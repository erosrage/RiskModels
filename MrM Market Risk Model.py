import numpy as np
import pandas as pd
import statsmodels.api as sm

# Example of stock and market returns
stock_returns = np.random.normal(0.001, 0.02, 252)
market_returns = np.random.normal(0.001, 0.015, 252)

# Add constant to the independent variable (market returns)
X = sm.add_constant(market_returns)

# OLS regression to calculate beta
model = sm.OLS(stock_returns, X).fit()
beta = model.params[1]
print(f"Stock Beta: {beta:.2f}")
