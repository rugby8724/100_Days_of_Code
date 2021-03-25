import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

response = requests.get('https://smile.amazon.com/KitchenAid-Classic-Quart-Tilt-Head-K45SSOB/dp/B003OXNBYC?ref_'
                        '=ast_sto_dp&th=1&psc=1')
response.raise_for_status()

web_product = response.text

print(web_product)
