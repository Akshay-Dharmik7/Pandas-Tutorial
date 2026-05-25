import pandas as pd

# read data from CSV file into dataframe
df1 = pd.read_csv("sales_data_sample.csv", encoding='latin1')
print(df1)

# read data from EXCEL file into dataframe
df2 = pd.read_excel("SampleSuperstore.xlsx")
print(df2)

# read data from JSON file into dataframe
df2 = pd.read_json("sample_Data.json")
print(df2)