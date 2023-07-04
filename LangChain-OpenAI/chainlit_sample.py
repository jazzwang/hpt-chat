import os
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import chainlit as cl

# Load OPENAI_API_KEY from .env
load_dotenv()

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=False)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=ChatOpenAI(temperature=0, streaming=True))

    return llm_chain