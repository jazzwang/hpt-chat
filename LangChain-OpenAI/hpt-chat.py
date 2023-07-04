import os
from dotenv import load_dotenv
## from LangChain
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
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
## from Chainlit - for Chatbot UI
import chainlit as cl

# Load OPENAI_API_KEY from .env
load_dotenv()

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=False)
def factory():
    ## LLM
    llm = ChatOpenAI(
        temperature=0,
        streaming=True,
    )
    ## LLMMathChain - for math related conversations
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    ## SQLDatabaseChain - for price related conversations
    db = SQLDatabase.from_uri("sqlite:///sample.db")
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)
    ## Tool for Agent
    tools = [
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
    ## create ZERO SHOT REACT Agent
    return initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs=agent_kwargs,
        memory=memory
    )