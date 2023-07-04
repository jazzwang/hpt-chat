## Reference:
## [1] https://python.langchain.com/docs/modules/agents/how_to/add_memory_openai_functions
## [2] https://github.com/ajndkr/lanarky/blob/main/examples/app/zero_shot_agent.py

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from langchain import (
    ConversationChain,
    LLMMathChain,
    OpenAI,
    SQLDatabase,
    SQLDatabaseChain,
)
from langchain.agents import AgentExecutor, AgentType, initialize_agent, load_tools, Tool
from langchain.chat_models import ChatOpenAI
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

from lanarky import LangchainRouter
from lanarky.testing import mount_gradio_app

load_dotenv()

def create_chain() -> AgentExecutor:
    llm = ChatOpenAI(
        temperature=0,
        streaming=True,
    )
    ## ConversationChain - for normal conversations
    chat = ConversationChain(llm=llm, verbose=True)
    ## LLMMathChain - for math related conversations
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    ## SQLDatabaseChain - for price related conversations
    db = SQLDatabase.from_uri("sqlite:///sample.db")
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)
    tools = [
        Tool(
            name="Chat",
            func=chat.run,
            description="useful for when you need to answer questions not related to math or price",
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math",
        ),
        Tool(
            name="Price",
            func=db_chain.run,
            description="useful for when you need to answer questions about price",
        ),
    ]
    ## For Memory
    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    return initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs=agent_kwargs,
        memory=memory
    )

app = mount_gradio_app(FastAPI(title="ZeroShotAgentDemo"))
templates = Jinja2Templates(directory="templates")
chain = create_chain()

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


langchain_router = LangchainRouter(
    langchain_url="/chat", langchain_object=chain, streaming_mode=1
)
langchain_router.add_langchain_api_route(
    "/chat_json", langchain_object=chain, streaming_mode=2
)
langchain_router.add_langchain_api_websocket_route("/ws", langchain_object=chain)

app.include_router(langchain_router)
