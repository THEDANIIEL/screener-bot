import requests as req
import pprint
import json

url=""

def get_pairs():

    response = req.get(
        "https://api.dexscreener.com/latest/dex/search?q=text",
        headers={"chainId": "solana"},
    )


    data = response.json()

    data = json.loads(data)

    filtered_list = [token for token in isinstance(data, dict) if token]

    print(filtered_list)

get_pairs()