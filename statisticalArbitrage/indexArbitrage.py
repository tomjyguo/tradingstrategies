import numpy as np
import pandas as pd
import yfinance as yf

def index_arbitrage(index_ticker, futures_ticker, start_date, end_date):
    data1 = yf.download(index_ticker, start=start_date, end=end_date)
    data2 = yf.download(futures_ticker, start=start_date, end=end_date)
    
    spread = data1['Close'] - data2['Close']
    
    spread_mean = spread.mean()
    spread_std = spread.std()
    
    z_score = (spread - spread_mean) / spread_std
    
    return spread, z_score

# Example Usage:
# stock1 = 'STOCK SYMBOL'
# stock2 = 'STOCK SYMBOL'
# start_date = 'yyyy-mm-dd'
# end_date = 'yyyy-mm-dd'

# Example Ticker:
# index_ticker = '^GSPC'    S&P 500 index
# futures_ticker = 'ES=F'   E-mini S&P 500 futures contract