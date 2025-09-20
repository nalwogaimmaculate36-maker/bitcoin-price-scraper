Python

# Bitcoin Price Scraper

# Author: Immaculate Nalwoga

# Description: Scrapes live Bitcoin price from CoinMarketCap and saves

# Step 1: Import libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import uuid
import os

# Step 2: Define target URL

url = 'https://coinmarketcap.com/currencies/bitcoin/'

# Step 3: Send request and parse HTML

response = request.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract coin name and price

coin_name_tag = soup.fin('h1', class='text-title')
price_tag = soup.find('span', class_='text-price')
