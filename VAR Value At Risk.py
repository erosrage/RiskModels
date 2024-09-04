import numpy as np
import pandas as pd

# Example of returns (you would typically load historical return data from a CSV or API)
returns = np.random.normal(0, 0.01, 1000)  # Simulated daily returns

# Parameters
confidence_level = 0.95  # 95% confidence level
time_horizon = 1  # 1 day
investment = 1000000  # $1,000,000

# Calculate VaR
VaR = np.percentile(returns, (1 - confidence_level) * 100) * investment
print(f"VaR (95% Confidence) over {time_horizon} day(s): ${-VaR:.2f}")
