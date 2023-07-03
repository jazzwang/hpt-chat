#!/usr/bin/env python

## Reference:
## [1] https://github.com/brunogarcia/langchain-titanic-sqlite
## [2] https://github.com/kemperd/langchain-sqlchain/blob/main/langchain-sqlchain.ipynb

import sys
from dotenv import load_dotenv
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

load_dotenv()
db = SQLDatabase.from_uri("sqlite:///sample.db")
llm = OpenAI(temperature=0)
db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)
db_chain.run(str(sys.argv[1]))
