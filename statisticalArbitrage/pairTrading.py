import numpy as np
import pandas as pd
import yfinance as yf

def pair_trading(stock1, stock2, start_date, end_date):
    data1 = yf.download(stock1, start=start_date, end=end_date)
    data2 = yf.download(stock2, start=start_date, end=end_date)
    
    spread = data1['Close'] - data2['Close']
    
    spread_mean = spread.mean()
    spread_std = spread.std()
    
    z_score = (spread - spread_mean) / spread_std
    
    return spread, z_score

# Example Usage:
# Define the stocks and time period:
# stock1 = 'STOCKNAME'
# stock2 = 'STOCKNAME'
# start_date = 'yyyy-mm-dd'
# end_date = 'yyyy-mm-dd'
