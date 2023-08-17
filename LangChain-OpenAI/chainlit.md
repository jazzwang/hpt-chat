# Welcome to Bacon Country Hospital! 🚀🤖

This is a POC Chatbot application based on the Machine Readable File (MRF) of Bacon Country Hospital.
The MRF file could be found from [here](https://assets.changehealthcare.com/Shop/PROD/static/BaconCountyHospital/ein_BaconCountyHospital_standardcharges.csv.zip).

## Sample questions

1. ask a question with simple syntax _**in Spanish**_

```
Por favor, proporciona el rango de precios de los procedimientos relacionados con RAYOS X.
Aseguradora: Aetna
```

ask a question with simple syntax _**in Japanese**_

```
X線に関連する最高料金はいくらですか?
```

ask a question with simple syntax _**in Chinese**_

```
睡眠呼吸中止症的最高價格
```

2. ask the average price with a fuzzy procedure name

```
What is the average price of IRON related procedure?
```

3. ask negotiated price with a fuzzy procedure name

```
What is the negotiated price of IRON related procedure?
```

4. ask with simple syntax like

```
price range: X-RAY related procedure
payer: Aetna
```

NOTE: `related procedure` is required for get the right SQL query using `LIKE '%X-RAY%'`

5. ask complex questions in bullet points

```
get the negotiated price of 3 procedures first and then give me the total amount:

- negotiated price of X-RAY related procedure
- negotiated price of IRON related procedure
- negotiated price of BED related procedure

Payer: Aetna
```
