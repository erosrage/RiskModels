import numpy as np

# Simulating returns using a normal distribution
mean_return = 0.001  # 0.1% average daily return
std_dev = 0.02  # 2% daily standard deviation
num_simulations = 10000
time_horizon = 252  # One year of trading days

# Generate random portfolio returns
random_returns = np.random.normal(mean_return, std_dev, (time_horizon, num_simulations))

# Simulate portfolio paths
initial_investment = 1000000
portfolio_paths = initial_investment * np.cumprod(1 + random_returns, axis=0)

# Analyze risk
final_returns = portfolio_paths[-1, :]
VaR_95 = np.percentile(final_returns, 5)
print(f"VaR (95%) after 1 year: ${initial_investment - VaR_95:.2f}")
