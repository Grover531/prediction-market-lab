import requests

from market import Market


"""
collector.py

Purpose: 
    Retrieve prediction market data and display it.

Version:
    v1
"""

def get_markets():
    url = "https://external-api.kalshi.com/trade-api/v2/markets"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    print("Collector started")
    print(get_markets())
    data = get_markets()
    print(type(data))
    

if __name__ == "__main__":
    main()