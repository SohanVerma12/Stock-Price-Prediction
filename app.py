import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from bokeh.sampledata.stocks import AAPL
from keras.models import load_model
import streamlit as st

start = '2010-01-01'
end = '2019-12-31'

st.title('Stock Price Prediction Model')

user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = data.DataReader(user_input , 'yahoo', start, end)

# Description
st.subheader('Date from 2010 - 2019')
st.write(df.describe())