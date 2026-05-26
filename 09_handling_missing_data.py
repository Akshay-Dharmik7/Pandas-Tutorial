import pandas as pd
import numpy as np

data = {
    "Name" : ["Akshay", "kartik", "rahul", "aman", "shyam", None, "gajodhar"],
    "Age" : [25, 21, 24, np.nan, 23, 25, 50],
    "Salary" : [30000, 23000, 40000, 45000, None, 20000, 35000],
    "Role" : ["Software Engineer", "Hr", "IT", "Sales Admin", "Client Partner", "Hr",  np.nan]
}

df = pd.DataFrame(data)

### 1. Detect Missing Values
# - Using isnull() or isna().
print(df.isnull()) # True or False

print(df.isna) #show NAN where missing values are present

# Count missing values
print(df.isnull().sum()) #column wise count

# Remove Rows with Missing Values
# print(df.dropna())

# Remove Columns with Missing Values
# print(df.dropna(axis=1))

# Fill with Constant Value
# print(df.fillna(0))

# Fill with Mean
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# print(df)

# # Fill with Median
# df["Age"] = df["Age"].fillna(df["Age"].median)
# print(df)

# Fill with Mode
# df["Age"] = df["Age"].fillna(df["Age"].mode()[0])
# print(df)

# Forward Fill
# print(df.ffill())

# Backward Fill
# print(df.bfill())

print(df["Age"].interpolate(method='linear'))
# print(df["Age"].interpolate(method='polynomial', order = 2))
# print(df["Age"].interpolate(method='time'))
