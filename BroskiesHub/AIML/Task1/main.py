
# Task 1: Build a Linear Regression Model (using California Housing Dataset)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# -----------------------------
# Load California Housing dataset
# -----------------------------
housing = fetch_california_housing(as_frame=True)
data = housing.frame

print("Dataset shape:", data.shape)
print(data.head())

# -----------------------------
# Select Features (1 or 2 for simplicity)
# -----------------------------
X = data[['MedInc']]   # Median Income in block group
y = data['MedHouseVal']  # Median House Value

# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)

print("Model Coefficient:", model.coef_)
print("Model Intercept:", model.intercept_)
print("RMSE:", rmse)
print("MAE:", mae)

# -----------------------------
# Visualization
# -----------------------------
plt.scatter(X_test, y_test, color="blue", alpha=0.5, label="Actual Prices")
plt.scatter(X_test, y_pred, color="red", alpha=0.5, label="Predicted Prices")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Linear Regression: Income vs House Value")
plt.legend()
plt.show()

