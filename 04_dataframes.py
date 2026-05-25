import pandas as pd

mydataset = {
    "Name" : ["Akshay", "Kartik", "Rohan"],
    "Age" : [25, 24, 27],
    "City" : ["Nagpur", "Jaipur", "Pune"],
    "Role" : ["Software Engineer", "HR", "IT Engieer"]
}

mydataframes = pd.DataFrame(mydataset)
print(mydataframes)

# specify index for dataframe

mydataset = {
    "Name" : ["Akshay", "Kartik", "Rohan"],
    "Age" : [25, 24, 27],
    "City" : ["Nagpur", "Jaipur", "Pune"]
}

mydataframes = pd.DataFrame(mydataset, index= ['Data1', 'Data2', 'Data3'])
print(mydataframes)