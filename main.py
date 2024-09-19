import requests
from bs4 import BeautifulSoup
from colorama import Fore
import json


url = "https://api.dexscreener.com/latest/solana"

tokens  = [] 

def get_tokens_list():

    res = requests.get(url, headers={},)

    if res.status_code != 200:
        print(Fore.RED + "can't fetch the data")

    tokens = res.json()


    print(tokens[0])

get_tokens_list()



