import numpy as np

# Example of portfolio returns and risk-free rate (e.g., US Treasury rate)
returns = np.random.normal(0.001, 0.02, 252)  # Simulated daily returns over a year
risk_free_rate = 0.01  # 1% annual risk-free rate

# Calculate annualized Sharpe ratio
excess_returns = returns - (risk_free_rate / 252)
sharpe_ratio = np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)
print(f"Annualized Sharpe Ratio: {sharpe_ratio:.2f}")
