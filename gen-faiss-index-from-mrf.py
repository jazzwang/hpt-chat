# coding: utf-8
import dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders.csv_loader import CSVLoader

# loads .env file with your OPENAI_API_KEY
dotenv.load_dotenv()

# CSV from https://gist.github.com/IvanCampos/94576c9746be280cf5b64083c8ea5b4d
loader = CSVLoader("sample.csv", csv_args = {"delimiter": ','})
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
faissIndex = FAISS.from_documents(docs, OpenAIEmbeddings())
faissIndex.save_local("bacon-mrf")
