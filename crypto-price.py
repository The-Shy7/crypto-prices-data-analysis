import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json

# page layout
# page expands to full width
st.set_page_config(layout="wide")

# title
st.title('Crypto Prices')
st.markdown(""" 
    This app retrieves cryptocurrency prices for the top 100 cryptocurrencies from **CoinMarketCap**
""")

# about 
expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Python libraries:** 
* **Data source:** [CoinMarketCap](http://coinmarketcap.com)
* **Credit:** Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by Bryan Feng
""")

# divide page to 3 columns
# col1 = sidebar, col2/col3 = page content
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

# sidebar + main panel
col1.header('Input Options')

# currency selector
currency_price_unit = col1.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))

# Web scraping of CoinMarketCap data
@st.cache # keep a cache of web scraping for subsequent use
def load_data():
    cmc = requests.get('https://coinmarketcap.com')
    soup = BeautifulSoup(cmc.content, 'html.parser')

    data = soup.find('script', id='__NEXT_DATA__', type='application/json')
    coins = {}
    coin_data = json.loads(data.contents[0])
    listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
    for i in listings:
        coins[str(i['id'])] = i['slug']

    coin_name = []
    coin_symbol = []
    market_cap = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []
    price = []
    volume_24h = []

    for i in listings:
        coin_name.append(i['slug'])
        coin_symbol.append(i['symbol'])
        price.append(i['quote'][currency_price_unit]['price'])
        percent_change_1h.append(i['quote'][currency_price_unit]['percent_change_1h'])
        percent_change_24h.append(i['quote'][currency_price_unit]['percent_change_24h'])
        percent_change_7d.append(i['quote'][currency_price_unit]['percent_change_7d'])
        market_cap.append(i['quote'][currency_price_unit]['market_cap'])
        volume_24h.append(i['quote'][currency_price_unit]['volume_24h'])

    df = pd.DataFrame(columns=['coin_name', 'coin_symbol', 'market_cap', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'price', 'volume_24h'])
    df['coin_name'] = coin_name
    df['coin_symbol'] = coin_symbol
    df['price'] = price
    df['percent_change_1h'] = percent_change_1h
    df['percent_change_24h'] = percent_change_24h
    df['percent_change_7d'] = percent_change_7d
    df['market_cap'] = market_cap
    df['volume_24h'] = volume_24h
    
    return df

df = load_data()