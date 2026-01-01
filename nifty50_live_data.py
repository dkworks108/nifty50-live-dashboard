import requests
import pandas as pd
import sys

sys.stdout.reconfigure(encoding="utf-8")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com/",
    "Connection": "keep-alive",
}

session = requests.Session()
session.headers.update(headers)

session.get("https://www.nseindia.com", timeout=10)

url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
response = session.get(url, timeout=10)

data = response.json()

df = pd.DataFrame(data["data"])

df = df[
    [
        "symbol",
        "open",
        "dayHigh",
        "dayLow",
        "previousClose",
        "lastPrice",
        "change",
        "pChange",
        "totalTradedVolume",
        "totalTradedValue",
        "yearHigh",
        "yearLow",
        "perChange30d",
    ]
]

df.columns = [
    "SYMBOL",
    "OPEN",
    "HIGH",
    "LOW",
    "PREV_CLOSE",
    "LTP",
    "CHNG",
    "%CHNG",
    "VOLUME (shares)",
    "VALUE (₹)",
    "52W H",
    "52W L",
    "30D %CHNG",
]

print("Total stocks:", len(df))
print(df)
