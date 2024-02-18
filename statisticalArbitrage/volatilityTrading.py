import numpy as np
import yfinance as yf
from scipy.stats import norm
from deltaPricing import delta

def black_scholes(S, K, T, r, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return option_price

def implied_volatility(S, K, r, T, option_price, sigma, tol, option_type):
    while True:
        price = black_scholes(S, K, T, r, sigma, option_type)
        vega = S * norm.pdf(d1) * np.sqrt(T)
        diff = price - option_price
        if abs(diff) < tol:
            break
        sigma -= diff / vega
    
    return sigma

def historical_volatility(prices):
    returns = np.log(prices / prices.shift(1)).dropna()
    volatility = returns.std() * np.sqrt(252)
    return volatility

def volatility_arbitrage(stock, option_symbol, start_date, end_date, K, option_type):
    stock_data = yf.download(stock, start=start_date, end=end_date)
    
    hist_volatility = historical_volatility(stock_data['Adj Close'])
    
    option_data = yf.Ticker(option_symbol)
    option_chain = option_data.option_chain(option_type)
    option_exp_date = option_chain.index[0]
    option_prices = option_chain.loc[option_exp_date]
    
    option_price = option_prices.loc[option_prices['strike'] == K]['lastPrice'].values[0]
    
    implied_vol = implied_volatility(stock_data['Adj Close'][-1], K, 0.05, (option_exp_date - stock_data.index[-1]).days / 365, option_price, option_type)
    
    if implied_vol > hist_volatility:
        print("Buy options - implied volatility is higher than historical volatility")
    elif implied_vol < hist_volatility:
        print("Sell options - implied volatility is lower than historical volatility")
    else:
        print("No arbitrage opportunity detected")

# Variables:
# stock: 'STOCK SYMBOL'
# option_symbol = 'AAPL220318C00200000'  (AAPL call option with strike price $200 and expiration date March 18, 2022 example)
# start_date = 'yyyy-mm-dd'
# end_date = 'yyyy-mm-dd'
# K: Strike price
# option_type = 'CALL/PUT'
# sigma: Initial volatility
# tol: Error tolerance
