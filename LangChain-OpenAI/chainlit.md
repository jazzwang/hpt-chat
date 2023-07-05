# Welcome to Bacon Country Hospital! 🚀🤖

This is a POC Chatbot application based on the Machine Readable File (MRF) of Bacon Country Hospital.
<br/>
The MRF file could be found from [here](https://assets.changehealthcare.com/Shop/PROD/static/BaconCountyHospital/ein_BaconCountyHospital_standardcharges.csv.zip).

## Sample questions

1. ask the average price with a fuzzy procedure name

```
What is the average price of IRON related procedure?
```

2. ask negotiated price with a fuzzy procedure name

```
What is the negotiated price of IRON related procedure?
```

3. ask with simple syntax like

```
price range: X-RAY related procedure
payer: Aetna
```

NOTE: `related procedure` is required for get the right SQL query using `LIKE '%X-RAY%'`

4. ask complex question

```
My father took multiple procedures including X-RAY related and IRON related. He needs a BED related procedure for 7 days. What is the total negotiated price for those 3 procedures? Payer is Aetna.
```

(this one sometimes fails)

5. ask complex questions in bullet points

```
get the negotiated price of 3 procedures first and then give me the total amount:

- negotiated price of X-RAY related procedure
- negotiated price of IRON related procedure
- negotiated price of BED related procedure

Payer: Aetna
```

6. ask complex questions using formula

```
SUM(
  negotiated price of X-RAY related procedure,negotiated price of IRON related procedure,negotiated price of BED related procedure
)

Payer: Aetna
```