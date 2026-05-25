import pandas as pd

mydataset = {
    "Name" : ["Akshay", "Kartik", "Rohan"],
    "Age" : [25, 24, 27],
    "City" : ["Nagpur", "Jaipur", "Pune"],
    "Role" : ["Software Engineer", "HR", "IT Engieer"]
}

df = pd.DataFrame(mydataset)

# save file as csv file with index
# df.to_csv("output_csv.csv")

# save file as csv file without index
df.to_csv("output_csv.csv", index= False)
df.to_excel("output_xlsx.xlsx", index= False)
df.to_json("output_json.json", index= False)

