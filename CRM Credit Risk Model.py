from sklearn.linear_model import LogisticRegression
import numpy as np

# Example features and default labels (1 = default, 0 = no default)
X = np.random.rand(1000, 3)  # Example features (e.g., financial ratios)
y = np.random.randint(0, 2, 1000)  # Default or not

# Logistic regression model for probability of default
model = LogisticRegression()
model.fit(X, y)

# Example of predicting probability of default
probability_of_default = model.predict_proba([[0.5, 0.4, 0.6]])[0][1]
print(f"Predicted Probability of Default: {probability_of_default:.2f}")
