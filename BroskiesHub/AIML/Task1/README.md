# Task 1: Build a Linear Regression Model

## 📌 Objective
Predict housing prices using a simple **linear regression model** with one or two features.

---

## 🛠 Tools & Libraries
- Python 3.x  
- pandas  
- numpy  
- scikit-learn  
- matplotlib  

---

## 📂 Dataset
We use the **California Housing dataset** (built into scikit-learn).  
- `MedInc` → Median income in block group (feature)  
- `MedHouseVal` → Median house value (target)

---

## 🚀 Steps Implemented
1. Import necessary libraries.  
2. Load the California Housing dataset.  
3. Select one feature (`MedInc`) to predict house prices.  
4. Split the dataset into training and testing sets using `train_test_split`.  
5. Train a **Linear Regression model**.  
6. Make predictions on test data.  
7. Evaluate the model using:  
   - RMSE (Root Mean Squared Error)  
   - MAE (Mean Absolute Error)  
8. Visualize actual vs predicted values with scatter plots.

---

## 📊 Results
- Outputs model coefficient and intercept.  
- Prints evaluation metrics (**RMSE, MAE**).  
- Displays a plot showing actual vs predicted house values.

---

## ▶️ How to Run
1. Clone this project or copy the files.  
2. Install required libraries (if not already installed):  
   ```bash
   pip install pandas numpy scikit-learn matplotlib
