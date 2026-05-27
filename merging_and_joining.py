import pandas as pd

df1 = pd.DataFrame({
    'ID': [1,2,3],
    'Name': ['Akshay','Rahul','Amit']
})

print(df1)

df2 = pd.DataFrame({
    'ID': [1,2,4],
    'Salary': [50000,60000,70000]
})

print(df2)

print("-------- Default Merge/Join (Inner Join) ---------------")
result = pd.merge(df1, df2, on="ID")
print(result)

print("--------- Left Join ------------------")
result = pd.merge(df1, df2, on="ID", how="left")
print(result)


print("--------- Right Join ------------------")
result = pd.merge(df1, df2, on="ID", how="right")
print(result)

print("--------- Outer Join ------------------")
result = pd.merge(df1, df2, on="ID", how="outer")
print(result)

# print('----------- Merge on Different Column Names ----------')
# error because Name is not present in both table
# result = pd.merge(df1, df2, left_on="ID", right_on="Name")
# print(result)

# print("---------- Merge Multiple Columns ----------")
# error because Name is not present in both table
# result = pd.merge(df1, df2, on=["ID", "Name"])
# print(result)



