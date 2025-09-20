{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "374bbf92-6d35-465e-9bab-ea74020fee2f",
   "metadata": {},
   "source": [
    "# In this project, we are going to be creating an automated web scraper.\n",
    "# Automated means it is going to scrap this data automatically, we will not need to keep runing the cell, the script in order for it to keep collecting the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "417e2f83-c5b9-44b6-8e07-07cd0946776e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f3c28d3-e049-4453-bc29-78a49d200711",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://coinmarketcap.com/currencies/bitcoin/'\n",
    "\n",
    "page = requests.get(url)\n",
    "\n",
    "soup = BeautifulSoup(page.text, 'html')\n",
    "\n",
    "print(soup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "882f987e-8cae-4d1a-a6ff-d3e0570832e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "<span data-role=\"coin-name\" title=\"Bitcoin\" class=\"sc-65e7f566-0 lsTl\">Bitcoin<span class=\"sc-65e7f566-0 eQBACe coin-name-mobile\"> price</span></span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f44f22e-1e3f-41da-9498-592b43f13ee7",
   "metadata": {},
   "outputs": [],
   "source": [
    "crypto_name = soup.find('span', class_ = 'sc-65e7f566-0 lsTl').text.replace('price','')\n",
    "\n",
    "print(crypto_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e4dd14a-8b8d-4274-88ea-f2495db4ab81",
   "metadata": {},
   "outputs": [],
   "source": [
    "<span class=\"sc-65e7f566-0 esyGGG base-text\" data-test=\"text-cdp-price-display\">$119,996.33</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63276939-e2c4-4fb1-af52-0e0b2bab6995",
   "metadata": {},
   "outputs": [],
   "source": [
    "crypto_price = soup.find('span', class_ = 'sc-65e7f566-0 esyGGG base-text').text.replace('$','')\n",
    "\n",
    "print(crypto_price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a34cd010-8652-4909-b2ca-a8597f41fabc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "date_time = datetime.now()\n",
    "\n",
    "print(date_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbb465fd-4089-4744-8d67-7b9f40bfb905",
   "metadata": {},
   "outputs": [],
   "source": [
    "datetime.now()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37425bfc-1d0b-4ff9-8194-18a5526d4511",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3179fc4b-80a7-4e30-9386-ce83aebaed08",
   "metadata": {},
   "outputs": [],
   "source": [
    "date_time = datetime.now()\n",
    "\n",
    "\n",
    "dict = ({'Crypto Name': crypto_name,\n",
    "        'Price': crypto_price,\n",
    "       'TimeStamp': date_time})\n",
    "\n",
    "df = pd.DataFrame([dict])\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "091ba520-194f-436d-9f5b-cc975817d403",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(r'C:\\Users\\nalwo\\Downloads\\Crytpo Automated Puller\\Crytpo_Automated_Pull.csv',index= False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5752090-3557-4002-b38d-f59d82d7b6fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cc13e75-776e-4930-9a26-62aa5e58c488",
   "metadata": {},
   "outputs": [],
   "source": [
    "if os.path.exists(r'C:\\Users\\nalwo\\Downloads\\Crytpo Automated Puller\\Crytpo_Automated_Pull.csv'):\n",
    "    df.to_csv(r'C:\\Users\\nalwo\\Downloads\\Crytpo Automated Puller\\Crytpo_Automated_Pull.csv',mode= 'a', header = False, index= False)\n",
    "else:\n",
    "    df.to_csv(r'C:\\Users\\nalwo\\Downloads\\Crytpo Automated Puller\\Crytpo_Automated_Pull.csv',index= False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae72ff97-dd5c-4cec-87a5-7470e70bb34e",
   "metadata": {},
   "source": [
    "# Let's put it together"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2f21d878-339e-41be-90d0-4a77c414f077",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "import os\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbe11ade-489e-4748-bdcb-d0dc665e2233",
   "metadata": {},
   "outputs": [],
   "source": [
    "def automated_crypto_pull():\n",
    "    url = 'https://coinmarketcap.com/currencies/bitcoin/'\n",
    "        \n",
    "    page = requests.get(url)\n",
    "        \n",
    "    soup = BeautifulSoup(page.text, 'html')\n",
    "        \n",
    "    crypto_name = soup.find('span',class_ = 'sc-65e7f566-0 lsTl').text.replace('price','')\n",
    "        \n",
    "    crypto_price = soup.find('span', class_ = 'sc-65e7f566-0 esyGGG base-text').text.replace('$','')\n",
    "     \n",
    "    date_time = datetime.now()\n",
    "        \n",
    "    dict = ({'Crypto Name': crypto_name,  'Price': crypto_price, 'TimeStamp': date_time})\n",
    "        \n",
    "    df = pd.DataFrame([dict])\n",
    "    print(df)\n",
    "    \n",
    "    if os.path.exists(r'C:\\Users\\nalwo\\Downloads\\Automated Crypto Puller\\Crytpo_Automated_Pull.csv'):\n",
    "        \n",
    "        df.to_csv(r'C:\\Users\\nalwo\\Downloads\\Automated Crypto Puller\\Crytpo_Automated_Pull.csv',mode= 'a', header = False, index= False)\n",
    "    else:\n",
    "        df.to_csv(r'C:\\Users\\nalwo\\Downloads\\Automated Crypto Puller\\Crytpo_Automated_Pull.csv',index= False)\n",
    "    print(df)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bbbe5931-5bfe-4670-bbbe-32e220875487",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Crypto Name       Price                  TimeStamp\n",
      "0    Bitcoin   118,293.07 2025-08-17 16:41:55.424083\n",
      "  Crypto Name       Price                  TimeStamp\n",
      "0    Bitcoin   118,293.07 2025-08-17 16:41:55.424083\n",
      "  Crypto Name       Price                  TimeStamp\n",
      "0    Bitcoin   118,252.41 2025-08-17 16:42:06.578927\n",
      "  Crypto Name       Price                  TimeStamp\n",
      "0    Bitcoin   118,252.41 2025-08-17 16:42:06.578927\n",
      "  Crypto Name       Price                  TimeStamp\n",
      "0    Bitcoin   118,252.41 2025-08-17 16:42:17.919080\n",
      "  Crypto Name       Price                  TimeStamp\n",
      "0    Bitcoin   118,252.41 2025-08-17 16:42:17.919080\n",
      "  Crypto Name       Price                  TimeStamp\n",
      "0    Bitcoin   118,252.41 2025-08-17 16:42:29.286756\n",
      "  Crypto Name       Price                  TimeStamp\n",
      "0    Bitcoin   118,252.41 2025-08-17 16:42:29.286756\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[0;32m      2\u001b[0m     automated_crypto_pull()\n\u001b[1;32m----> 3\u001b[0m     time\u001b[38;5;241m.\u001b[39msleep(\u001b[38;5;241m10\u001b[39m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    automated_crypto_pull()\n",
    "    time.sleep(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10320c66-b964-4fd0-8038-53145339ec01",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd702e46-50ce-4764-834e-6b907b670770",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8693baa1-1009-44aa-a2de-d4d45f20f729",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44f200c2-e05b-42ca-aa1a-0cdda6e06f9a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e71c09b-2d30-4484-8cdc-0876c7aa37b3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9f2f9e9-606c-4d4d-8b7b-77a2c4c8e295",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dcb6b4d-385b-446c-8114-43fa4c135fa9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c5ce2ce-3470-49cb-8397-1f1f828dd5f7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2121ff8-c41c-4f85-80b5-1af4d681564e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b3daea5-9a3f-4a28-9726-64b8b75a643f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05872877-b1b4-426b-a5f1-faf1ff0dc7f4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b227174-cdf4-416a-ada8-7db18ef0006e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54d1166f-3695-4e70-b3b0-b774b729b30e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4417ef4-f08f-4edc-ad97-b3bfb14e866d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0cc431b-07f8-4dc6-a3ed-eb8c98e80689",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d29d1b85-601b-40ff-8812-5970763db6ec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "603b0e09-4ff1-4b94-9711-c88e07479c12",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f7c53a1-059a-442a-af28-8c7fd2dabdd0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53be2e13-6181-44fd-905f-29a4d1a8e180",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c366cbde-7d91-4984-9d2e-05aad7787c19",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "256ea010-a410-4a33-a719-a04d596bac87",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34e55f0c-afcf-4aec-8a01-d21ee9f007e9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16c89668-5a2e-4425-8860-17e58afaf054",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "076375ea-c902-440f-8b01-8f724969be51",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ff107ba-f858-4323-9574-5b378b955dac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b3f010e-7b91-4043-b7bd-ff2807a1629d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b4f48b5-5463-4fa1-bd70-96660da83da9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc8c206e-223a-4695-b452-b531d8b72d14",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb233f0c-6150-4531-b577-2c1909a339c3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23070faa-4cea-4f9d-a51f-3d0ab7dda57d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff4fff6d-a3e0-420f-9644-f631bca5a238",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2244d5b4-839f-4b54-a742-b4483527c76b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25e60d6c-1e65-483c-b860-3db890979b7c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "983f0bbc-ac7f-4e7d-b39a-9e7998d07953",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a98b9e2e-9e49-42eb-b8e9-98ecee703d6e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4216735d-e5b2-46c5-aaa5-c4d2520c1e19",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd36a1bc-a4e2-491b-8e3a-90127a11c5ad",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5944cd3-2922-43a9-851f-f8cf49028b1e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b25b4798-6f1f-499a-80e2-e71bdc29fc66",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4938484b-9162-4810-8740-49e7b901b404",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d6c5159-e033-490d-8a3e-b8b7a4d383e6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
