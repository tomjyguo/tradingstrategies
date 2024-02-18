import numpy as np

def smooth_payoff(payoff, smoothing_factor):
    # Initialize array to store smoothed payoff
    smoothed_payoff = np.zeros_like(payoff)

    # Apply smoothing to the payoff
    for i in range(1, len(payoff)):
        smoothed_payoff[i] = smoothing_factor * payoff[i] + (1 - smoothing_factor) * smoothed_payoff[i-1]

    return smoothed_payoff

# Example usage:
# payoff = np.array([0, 5, 10, 8, 12])
# smoothing_factor = 0.2
