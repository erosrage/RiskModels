import numpy as np

# Example returns (you can replace this with actual portfolio returns)
returns = np.random.normal(0, 0.01, 1000)

# Parameters
confidence_level = 0.95

# Calculate VaR
VaR = np.percentile(returns, (1 - confidence_level) * 100)

# Calculate ES (mean of losses beyond VaR)
expected_shortfall = returns[returns <= VaR].mean()
print(f"Expected Shortfall (95% Confidence): {-expected_shortfall:.4f}")
