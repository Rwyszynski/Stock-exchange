import pandas as pd
import wget
import matplotlib
import requests
import json


response = requests.get(
    'https://financialmodelingprep.com/api/v3/historical-chart/5min/AAPL?from=2024-05-27&to=2024-06-27&apikey=1naOu5k2WMCBylHjrlsRplGrDXNdSsqt').json()

df = pd.DataFrame(columns=["date", "open", "low", "high", "close", "volume"])
for i in range(0, len(response)):
    currentItem = response[i]
    df.loc[i] = [response[i]["date"], response[i]["open"], response[i]["low"],
                 response[i]["high"], response[i]["close"], response[i]["volume"]]
print(df)
