## 0. REQUIREMENT

### 0.1 OPENAI API KEY

- get OPENAI_API_KEY from https://platform.openai.com/account/api-keys
```
~/git/shop-client-poc$ cp .env.sample .env
```
replace with your API key.
```
~/git/shop-client-poc$ echo "OPENAI_API_KEY=sk-......." > .env
```

### 0.2 LangChain package

```
~/git/shop-client-poc$ pip install -r requirements.txt
```

# 1. How to run

```bash
~/git/shop-client-poc$ make
```
or
```bash
~/git/shop-client-poc$ ./gen-sqlite-from-mrf.sh
~/git/shop-client-poc$ pip install -r requirements.txt
~/git/shop-client-poc$ ./bacon.py "YOUR QUESTION"
```
* NOTE: tested success with Python 3.11. test fail with Python 3.8

## 2. Examples

```bash
gitpod /workspace/gitpod-labs/shop-chat-poc (master) $ make
--2023-06-29 04:28:31--  https://assets.changehealthcare.com/Shop/PROD/static/BaconCountyHospital/ein_BaconCountyHospital_standardcharges.csv.zip
Resolving assets.changehealthcare.com (assets.changehealthcare.com)... 45.60.195.19
Connecting to assets.changehealthcare.com (assets.changehealthcare.com)|45.60.195.19|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 536516 (524K) [application/zip]
Saving to: ‘ein_BaconCountyHospital_standardcharges.csv.zip’

ein_BaconCountyHospital_standardcharges.csv 100%[===========================================================================================>] 523.94K   307KB/s    in 1.7s    

2023-06-29 04:28:33 (307 KB/s) - ‘ein_BaconCountyHospital_standardcharges.csv.zip’ saved [536516/536516]

Archive:  ein_BaconCountyHospital_standardcharges.csv.zip
  inflating: 58-2224545_BaconCountyHospital_standardcharges.csv  
CREATE TABLE IF NOT EXISTS "MRF"(
  "PRIMARY_PROCEDURE_DESCRIPTION" TEXT,
  "SETTING_TYPE" TEXT,
  "SERVICE_COMPONENT_BREAKOUT_TYPE" TEXT,
  "SERVICE_COMPONENT_BREAKOUT_NAME" TEXT,
  "DRG_CODE" TEXT,
  "CPT_CODE" TEXT,
  "MODIFIER" TEXT,
  "HCPCS_CODE" TEXT,
  "REV_CODE" TEXT,
  "GROSS_PRICE" TEXT,
  "CASH_PRICE" TEXT,
  "NEGOTIATED_PRICE" TEXT,
  "DEIDENTIFIED_MIN_PRICE" TEXT,
  "DEIDENTIFIED_MAX_PRICE" TEXT,
  "PAYER_NAME" TEXT,
  "NETWORK_NAME" TEXT
);
"HOSPICE BED","","","","","","","",0111,704.00,704.00,1000.00,512.09,1966.57,Aetna,MCRX
"HOSPICE BED","","","","","","","",0111,704.00,704.00,512.09,512.09,1966.57,BCBS,"All Other Products"
"HOSPICE BED","","","","","","","",0111,704.00,704.00,1947.10,512.09,1966.57,BCBS,MCRX
"HOSPICE BED","","","","","","","",0111,704.00,704.00,559.68,512.09,1966.57,BCBS,Preferred
"HOSPICE BED","","","","","","","",0111,704.00,704.00,1966.57,512.09,1966.57,Humana,"MCRX PPO"
Requirement already satisfied: langchain in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from -r requirements.txt (line 1)) (0.0.206)
Requirement already satisfied: openai in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from -r requirements.txt (line 2)) (0.27.8)
Requirement already satisfied: python-dotenv in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from -r requirements.txt (line 3)) (1.0.0)
Requirement already satisfied: sqlalchemy in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from -r requirements.txt (line 4)) (2.0.16)
Requirement already satisfied: PyYAML>=5.4.1 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (6.0)
Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (3.8.4)
Requirement already satisfied: dataclasses-json<0.6.0,>=0.5.7 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (0.5.8)
Requirement already satisfied: langchainplus-sdk>=0.0.13 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (0.0.16)
Requirement already satisfied: numexpr<3.0.0,>=2.8.4 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (2.8.4)
Requirement already satisfied: numpy<2,>=1 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (1.25.0)
Requirement already satisfied: openapi-schema-pydantic<2.0,>=1.2 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (1.2.4)
Requirement already satisfied: pydantic<2,>=1 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (1.10.9)
Requirement already satisfied: requests<3,>=2 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (2.28.2)
Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (8.2.2)
Requirement already satisfied: tqdm in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from openai->-r requirements.txt (line 2)) (4.65.0)
Requirement already satisfied: typing-extensions>=4.2.0 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from sqlalchemy->-r requirements.txt (line 4)) (4.5.0)
Requirement already satisfied: greenlet!=0.4.17 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from sqlalchemy->-r requirements.txt (line 4)) (2.0.2)
Requirement already satisfied: attrs>=17.3.0 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (22.2.0)
Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (3.1.0)
Requirement already satisfied: multidict<7.0,>=4.5 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (6.0.4)
Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (4.0.2)
Requirement already satisfied: yarl<2.0,>=1.0 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (1.9.2)
Requirement already satisfied: frozenlist>=1.1.1 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (1.3.3)
Requirement already satisfied: aiosignal>=1.1.2 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (1.3.1)
Requirement already satisfied: marshmallow<4.0.0,>=3.3.0 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain->-r requirements.txt (line 1)) (3.19.0)
Requirement already satisfied: marshmallow-enum<2.0.0,>=1.5.1 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain->-r requirements.txt (line 1)) (1.5.1)
Requirement already satisfied: typing-inspect>=0.4.0 in /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain->-r requirements.txt (line 1)) (0.9.0)
Requirement already satisfied: idna<4,>=2.5 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from requests<3,>=2->langchain->-r requirements.txt (line 1)) (3.4)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from requests<3,>=2->langchain->-r requirements.txt (line 1)) (1.26.15)
Requirement already satisfied: certifi>=2017.4.17 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from requests<3,>=2->langchain->-r requirements.txt (line 1)) (2022.12.7)
Requirement already satisfied: packaging>=17.0 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from marshmallow<4.0.0,>=3.3.0->dataclasses-json<0.6.0,>=0.5.7->langchain->-r requirements.txt (line 1)) (23.0)
Requirement already satisfied: mypy-extensions>=0.3.0 in /home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages (from typing-inspect>=0.4.0->dataclasses-json<0.6.0,>=0.5.7->langchain->-r requirements.txt (line 1)) (1.0.0)


> Entering new  chain...
count of distinct cpt
SQLQuery:SELECT COUNT(DISTINCT "CPT_CODE") FROM "MRF"
SQLResult: [(1229,)]
Answer:There are 1229 distinct CPT codes.
> Finished chain.
Usage: ./bacon.py 'your question'
gitpod /workspace/gitpod-labs/shop-chat-poc (master) $ make test


> Entering new  chain...
count of primary precedures
SQLQuery:SELECT COUNT(DISTINCT "PRIMARY_PROCEDURE_DESCRIPTION") FROM "MRF"
SQLResult: [(4532,)]
Answer:There are 4532 distinct primary procedures.
> Finished chain.


> Entering new  chain...
price of IRON related precedures
SQLQuery:SELECT "PRIMARY_PROCEDURE_DESCRIPTION", "GROSS_PRICE", "CASH_PRICE", "NEGOTIATED_PRICE" FROM "MRF" WHERE "PRIMARY_PROCEDURE_DESCRIPTION" LIKE '%IRON%' LIMIT 5;
SQLResult: [('IRON', '76.00', '76.00', '24.32'), ('IRON', '76.00', '76.00', '25.60'), ('IRON', '76.00', '76.00', '55.28'), ('IRON', '76.00', '76.00', '21.28'), ('IRON', '76.00', '76.00', '60.42')]
Answer:The price of IRON related procedures ranges from 21.28 to 60.42.
> Finished chain.
gitpod /workspace/gitpod-labs/shop-chat-poc (master) $ 
gitpod /workspace/gitpod-labs/shop-chat-poc (master) $ ./bacon.py "list columns of database"


> Entering new  chain...
list columns of database
SQLQuery:SELECT * FROM MRF LIMIT 5;
SQLResult: [('HOSPICE BED', '', '', '', '', '', '', '', '0111', '704.00', '704.00', '1000.00', '512.09', '1966.57', 'Aetna', 'MCRX'), ('HOSPICE BED', '', '', '', '', '', '', '', '0111', '704.00', '704.00', '512.09', '512.09', '1966.57', 'BCBS', 'All Other Products'), ('HOSPICE BED', '', '', '', '', '', '', '', '0111', '704.00', '704.00', '1947.10', '512.09', '1966.57', 'BCBS', 'MCRX'), ('HOSPICE BED', '', '', '', '', '', '', '', '0111', '704.00', '704.00', '559.68', '512.09', '1966.57', 'BCBS', 'Preferred'), ('HOSPICE BED', '', '', '', '', '', '', '', '0111', '704.00', '704.00', '1966.57', '512.09', '1966.57', 'Humana', 'MCRX PPO')]
Answer:The columns of the database are PRIMARY_PROCEDURE_DESCRIPTION, SETTING_TYPE, SERVICE_COMPONENT_BREAKOUT_TYPE, SERVICE_COMPONENT_BREAKOUT_NAME, DRG_CODE, CPT_CODE, MODIFIER, HCPCS_CODE, REV_CODE, GROSS_PRICE, CASH_PRICE, NEGOTIATED_PRICE, DEIDENTIFIED_MIN_PRICE, DEIDENTIFIED_MAX_PRICE, PAYER_NAME, and NETWORK_NAME.
> Finished chain.
gitpod /workspace/gitpod-labs/shop-chat-poc (master) $ ./bacon.py "list name of databases"


> Entering new  chain...
list name of databases
SQLQuery:SELECT name FROM sqlite_master WHERE type='table';
SQLResult: [('MRF',)]
Answer:The name of the database is MRF.
> Finished chain.
```