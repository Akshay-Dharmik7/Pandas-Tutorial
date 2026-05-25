import pandas as pd


df = pd.read_csv('sales_data_sample.csv', encoding="latin1")

#head()
print("---------- first 5 data ------------")
print(df.head())   #first 5 data

print("---------- first 10 data ------------")
print(df.head(10))  #first 10 data

# tail()
print("---------- last 5 data ------------")
print(df.tail())   #last 5 data

print("---------- last 10 data ------------")
print(df.tail(10))  #last 10 data

# info()
print("-------------- Information of dataset ----------------")
print(df.info())


# describe()
print("-------------- Describe of dataset ----------------")
print(df.describe())
