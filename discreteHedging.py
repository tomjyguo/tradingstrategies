import numpy as np

def discrete_hedging(S, P, K, n):
    # Initialize arrays to store hedging parameters
    delta = np.zeros(n)
    hedge_portfolio_value = np.zeros(n)

    # Perform discrete hedging over time steps
    for t in range(n):
        delta[t] = np.where(P[t] > K, 1.0, 0.0)
        hedge_portfolio_value[t] = delta[t] * P[t] - delta[t-1] * P[t-1]

    return hedge_portfolio_value.sum() - S

# Variables:
# S: Option price
# P: Underlying price
# K: Strike price
# n: Number of steps
