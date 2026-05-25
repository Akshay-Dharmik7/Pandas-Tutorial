import pandas as pd

myseries = pd.Series([1, 2, 3, 4, 5, 6])
print(myseries)

mydataset = {  
  'cars': ["BMW", "Volvo", "Ford"],  
  'passings': [3, 7, 2]  
}
mydataframes = pd.DataFrame(mydataset)
print(mydataframes)

