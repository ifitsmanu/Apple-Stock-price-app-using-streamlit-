import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
        ## Simple Stock Price App


        shown are the stock **closing price** and ***volume*** of Apple!

        """)

#https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol

trickerSymbol = 'AAPL'

#get data on this ticker

tickerdata = yf.Ticker(trickerSymbol)

#get the historical prices for this ticker
tickerDF = tickerdata.history(period='1d', start='2010-5-31', end='2022-5-31')

# open high low close volume dividends stock splits

st.write("""
        ## Closing Price
        """)
st.line_chart(tickerDF.Close)
st.write("""
        ## Volume Price
        """)
st.line_chart(tickerDF.Volume)
