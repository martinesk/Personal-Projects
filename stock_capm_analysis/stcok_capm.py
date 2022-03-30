import pandas as pd
import seaborn as sns
import plotly.express as px
from copy import copy
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st

stocks_df = pd.read_csv('stocks_dataset.csv')


#normalize price
def normalize(df):
  x = df.copy()
  for i in x.columns[1:]:
    x[i] = x[i]/x[i][0]
  return x
print(normalize(stocks_df).head())


#plot charts
def interactive_plot(df, title):
  fig = px.line(title = title)
  for i in df.columns[1:]:
    fig.add_scatter(x = df['Date'], y = df[i], name = i)
  fig.show()

interactive_plot(stocks_df,"Prices")

#daily returns
def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns[1:]:

        for j in range(1, len(df)):
            # Calculate the percentage of change from the previous day
            df_daily_return[i][j] = ((df[i][j] - df[i][j - 1]) / df[i][j - 1]) * 100
        df_daily_return[i][0] = 0
    return df_daily_return

stocks_daily_return = daily_return(stocks_df)
stocks_daily_return.plot(kind = 'scatter', x = 'sp500', y = 'TSLA', color = 'w')
beta, alpha = np.polyfit(stocks_daily_return['sp500'], stocks_daily_return['TSLA'], 1)
plt.plot(stocks_daily_return['sp500'], beta * stocks_daily_return['sp500'] + alpha, '-', color = 'r')
plt.show()
