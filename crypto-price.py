import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
""")

# divide page to 3 columns
# col1 = sidebar, col2/col3 = page content
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

# sidebar + main panel
col1.header('Input Options')

# currency selector
currency_price_unit = col1.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))
