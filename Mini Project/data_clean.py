#importing neccesary libraries
import pandas as pd
import numpy as np

# loading dataset
df = pd.read_csv("Mini Project\employee_practice_data.csv")
print(df.head())

# checking the missing value
print("Missing values in each column")
print(df.isnull().sum())

df['Salary (INR)'].fillna(df["Salary (INR)"].mean(), inplace=True)

df["Performance Rating"].fillna(df["Performance Rating"].median(), inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df.fillna(df.mean(numeric_only=True), inplace=True)

# round the experience if it is filled with decimal values
df["Experience (Years)"] = df["Experience (Years)"].round(0)

# round the performance rating if it is filled with decimal values
df["Performance Rating"] = df["Performance Rating"].round(1)

# remove duplicate records
df.drop_duplicates(inplace=True)

# replace negative salaries 
df["Salary (INR)"] = np.where(df["Salary (INR)"] < 0, df["Salary (INR)"].mean(), df["Salary (INR)"])

salary_mean = df["Salary (INR)"].mean()
salary_std = df["Salary (INR)"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# remove rows where salary is too high or too low.
df = df[(df["Salary (INR)"] >= lower_bound) & df["Salary (INR)"] <= upper_bound]

df.to_csv("Mini Project\cleaned_indian_employee_data.csv", index = False)

print('Data cleaning is completed! Saved as "cleaned_indian_employee_data.csv"')
