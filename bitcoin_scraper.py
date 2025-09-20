# Python

# Bitcoin Price Scraper

# Author: Immaculate Nalwoga

# Description: Scrapes live Bitcoin price from CoinMarketCap and appends

# Step 1: Import libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import os
  
# Step 2: Define scraping function

def automated_crypto_pull():
  url = 'https://coinmarketcap.com/currencies/bitcoin/'
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')

  # Step 3: Extract crypto name and price

  crypto_name = soup.find('span', class_='sc-65e7f566-0 lsTl').text.replace('price', '')
  crypto_price = soup.find('span', class_='sc-65e7f566-0 esyGGG base-text').text.replace('$', '')
  date_time = datetime.now()


  # Step 4: Structure data

  data = {
        'Crypto Name': crypto_name,
        'Price': crypto_price,
        'Timestamp': date_time
        }

  df = pd.DataFrame([data])
  print(df)
  
  # Step 5: Save to CSV
  csv_path = r'C:\Users\nalwo\Downloads\Automated Crypto Puller\Crytpo_Automated_Pull.csv'
  if os.path.exists(csv_path):
      df.to_csv(csv_path, mode='a', header=False, index=False)
  else:
      df.to_csv(csv_path, index=False)

# Step 6: Structure data into dictionary

while True:
  automated_crypto_pull()
  time.sleep(600)  # Wait 10 minutes befor next scrape
