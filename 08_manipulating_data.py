import pandas as pd

data = {
    "Name" : ["Akshay", "kartik", "rahul", "aman", "shyam", "madhav", "gajodhar"],
    "Age" : [25, 21, 24, 32, 23, 25, 50],
    "Salary" : [30000, 23000, 40000, 45000, 32000, 20000, 35000],
    "Role" : ["Software Engineer", "Hr", "IT", "Sales Admin", "Client Partner", "Hr",  "Team Lead"]
}

df = pd.DataFrame(data)
print(df)

print("*" * 70)

# Adding new column
df["Location"] = ["Pune", "Jaipur", "Delhi", "Jaipur", "Mumbai", "Hyderabad", "Benglore"]
print(df)

print("*" * 70)

# Adding new column at specific position.
df.insert(3, "Bonus", df["Salary"] * 0.1)
print(df)

print("--------------- drop single row ----------------")
# delete single row
df2 = df.drop(1, inplace=True)
print(df)


print("--------------- drop column ----------------")
# Deleting column
df.drop(columns = ["Location"], inplace=True)
print(df)

print("--------------- drop multiple column ----------------")
# deleting multiple columns
df.drop(columns = ["Location", "Bonus"], inplace=True, errors= 'ignore')
print(df)



print("--------------- update value loc[] ----------------")
# updating data from datafram
df.loc[0, 'Salary'] = 50000
print(df)

print("--------------- update value iloc[] ----------------")
# updating data from datafram
df.iloc[0, 2] = 60000
print(df)




