#####
## 2024-06-24 Update: MRF website is no longer available due to CHC Cyberattach on Feb 21, 2024
#####
# DOWNLOAD
# wget https://assets.changehealthcare.com/Shop/PROD/static/BaconCountyHospital/ein_BaconCountyHospital_standardcharges.csv.zip
# UNZIP and SAMPLE
# unzip ein_BaconCountyHospital_standardcharges.csv.zip
# REMOVE ZIP
# rm *.zip
# remove top 3 lines
# grep '","' 58-2224545_BaconCountyHospital_standardcharges.csv > sample.csv
sqlite3 sample.db < import.sql
#rm *.csv
