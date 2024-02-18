import numpy as np
from scipy.stats import norm

def delta(S, K, r, T, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    delta = norm.cdf(d1)
    return delta

# Variable:
# S: Current price
# K: Strike price
# r: Risk-free interest rate
# T: Time to expiration (years)
# sigma: Volatility
