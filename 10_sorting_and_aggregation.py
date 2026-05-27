import pandas as pd

data = {
    'Name': ['Akshay', 'Rahul', 'Amit', 'Karan','Neha'],
    'Age': [25, 24, 26, 24, 23],
    'Marks': [85, 90, 78, 85, 88]
}

df = pd.DataFrame(data)

print(df)

# sort_values()
# 1. Sort by Single Column
print("--------- Sort by Single Column ----------")
sorted_df = df.sort_values(by="Age")
print(sorted_df)

# 2. Descending Order
print("----------- Descending Order ------------")
desc_sorted_df = df.sort_values(by="Age", ascending=False)
print(desc_sorted_df)

# 3. Sort by Multiple Columns
print("-------- Sort by Multiple Columns -----------")
multi_col_sorted_df = df.sort_values(by=["Age", "Marks"])
print(multi_col_sorted_df)


# sort_index()
print("-------- Sort by Index -----------")
print(df.sort_index())


print("------------------------------------------------------")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("------------------------------------------------------")

print("-------------- SUM() ----------------")
print(df.sum())
print(df["Age"].sum())
print(df["Marks"].sum())

print("-------------- MEAN() ----------------")
print(df["Age"].mean())
print(df["Marks"].mean())

print("--------------- MIN() ---------------")
print(df.min())
print(df["Age"].min())
print(df["Marks"].min())

print("--------------- MAX() ---------------")
print(df.max())
print(df["Age"].max())
print(df["Marks"].max())

print("------------- COUNT() --------------")
print(df.count())
print(df["Age"].count())
print(df["Marks"].count())

print("------------- STD() -------------")
# print(df.std()) #error
print(df["Age"].std)
print(df["Marks"].std)

print("------------ MEDIAN() --------------")
# print(df.median()) #error
print(df["Age"].median())
print(df["Marks"].median())

# print("---------- Multiple Aggregate function ---------")
print(df["Age"].agg(["sum", "min", "max", "mean", "count", "std", "median"]))