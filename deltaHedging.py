import numpy as np
from scipy.stats import norm

def black_scholes_delta(S, K, T, r, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option_type == 'call':
        delta = norm.cdf(d1)
    else:
        delta = norm.cdf(d1) - 1
    return delta

def delta_hedging(S, K, T, r, sigma, d_0, option_price, frequency):
    dt = 1 / 252
    total_days = T * 252
    hedge_interval = int(total_days / frequency)
    
    hedge_dates = np.linspace(0, total_days, frequency + 1)[1:]
    
    portfolio_value = d_0 * S - option_price 
    cumulative_pnl = 0
    
    for i in range(frequency):
        t = hedge_dates[i]
        S_t = S * np.exp((r - 0.5 * sigma**2) * t + sigma * np.sqrt(t) * np.random.randn())

        if option_type == 'call':
            delta_t = black_scholes_delta(S_t, K, T - (t / 252), r, sigma, option_type='call')
        else:
            delta_t = black_scholes_delta(S_t, K, T - (t / 252), r, sigma, option_type='put')

        hedge_quantity = delta_t - d_0
        pnl = hedge_quantity * (S_t - S)
        cumulative_pnl += pnl
        portfolio_value += pnl
        
        d_0 = delta_t
        
    return cumulative_pnl, portfolio_value

# Variables:
# S: Initial price
# K: Strike price
# T: Time to expiration (years)
# r: Annual risk-free interest rate
# sigma: Volatility
# d_0: Initial delta of the option
# option_price: Initial price of the option (Black-Scholes)
# frequency:  Number of delta hedge per day
