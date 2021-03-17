import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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