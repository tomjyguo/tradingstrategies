import numpy as np

def discrete_hedging(option_price, underlying_price, strike_price, num_steps):
    # Initialize arrays to store hedging parameters
    delta = np.zeros(num_steps)
    hedge_portfolio_value = np.zeros(num_steps)

    # Perform discrete hedging over time steps
    for t in range(num_steps):
        # Determine delta (hedge ratio) at each time step
        delta[t] = np.where(underlying_price[t] > strike_price, 1.0, 0.0)
        # Calculate the change in portfolio value due to delta adjustments
        hedge_portfolio_value[t] = delta[t] * underlying_price[t] - delta[t-1] * underlying_price[t-1]

    # Calculate the total profit and loss from the hedging strategy
    return hedge_portfolio_value.sum() - option_price

# Example usage:
# option_price = 5.0
# underlying_price = np.array([100, 102, 98, 105, 97])
# strike_price = 100
# num_steps = len(underlying_price)

# discrete_hedging(option_price, underlying_price, strike_price, num_steps)