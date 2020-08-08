# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:40:59 2020

@author: Alexrios22
"""


# Import necesary libraries
import yfinance as yf 
import talib as ta
import matplotlib.pyplot as plt

ticker = "INTC"
ohlcv = yf.download(ticker, period="1y", interval="1d", auto_adjust=True) 

#Overlap Studies Functions
#Moving Average
ohlcv['Simple MA'] = ta.SMA(ohlcv['Close'],10)
ohlcv['EMA'] = ta.EMA(ohlcv['Close'], timeperiod = 20)
ohlcv['WMA'] = ta.WMA(ohlcv['Close'], timeperiod = 50)
# Plot
ohlcv[['Close','Simple MA','EMA','WMA']].plot(figsize=(15,15))
plt.show()

# Bollinger Bands
ohlcv['upper_band'], ohlcv['middle_band'], ohlcv['lower_band'] = ta.BBANDS(ohlcv['Close'], timeperiod =20)
# Plot
ohlcv[['Close','upper_band','middle_band','lower_band']].plot(figsize=(15,15))
plt.show()

#Momentum Indicator Functions
ohlcv['RSI'] = ta.RSI(ohlcv['Close'],14)
ohlcv['macd'], ohlcv['macdsignal'],ohlcv['macdhist'] = ta.MACD(ohlcv['Close'], 
                                                               fastperiod=12, 
                                                               slowperiod=26, 
                                                               signalperiod=9)
ohlcv['slowk'], ohlcv['slowd'] = ta.STOCH(ohlcv['High'], ohlcv['Low'],
                                          ohlcv['Close'], fastk_period=14, 
                                          slowk_period=3, slowk_matype=0, 
                                          slowd_period=3, slowd_matype=0)

ohlcv = ohlcv.reset_index()
fig, axs = plt.subplots(4)
fig.suptitle('RSI - MACD - Stochastic')
axs[0].plot(ohlcv['Date'],ohlcv['Close'])
axs[1].plot(ohlcv['Date'],ohlcv['RSI'],color='Red')
axs[2].plot(ohlcv['Date'],ohlcv['macd'],ohlcv['Date'], ohlcv['macdsignal'])
axs[3].plot(ohlcv['Date'],ohlcv['fastk'],ohlcv['Date'], ohlcv['fastd'])

# Hide x labels and tick labels for all but bottom plot.
for ax in axs:
    ax.label_outer()
    
#Volume Indicator Functions
ohlcv['OBV'] = ta.OBV(ohlcv['Close'],ohlcv['Volume'])

fig, axs = plt.subplots(2)
fig.suptitle('On Balance Volume')
axs[0].plot(ohlcv['Date'],ohlcv['Close'])
axs[1].plot(ohlcv['Date'],ohlcv['OBV'],color='Red')
# Hide x labels and tick labels for all but bottom plot.
for ax in axs:
    ax.label_outer()
    
#Volatility Indicator Functions
ohlcv['ATR'] = ta.ATR(ohlcv['High'], ohlcv['Low'], ohlcv['Close'], 
                      timeperiod=14)

fig, axs = plt.subplots(2)
fig.suptitle('Average True Range')
axs[0].plot(ohlcv['Date'],ohlcv['Close'])
axs[1].plot(ohlcv['Date'],ohlcv['ATR'],color='Red')
# Hide x labels and tick labels for all but bottom plot.
for ax in axs:
    ax.label_outer()
    
#Pattern Recognition Functions
ohlcv['BELTHOLD'] = ta.CDLBELTHOLD(ohlcv['Open'], ohlcv['High'], 
                                            ohlcv['Low'], ohlcv['Close'])

print(ohlcv.head())