import pandas as pd

myseries = pd.Series([1, 2, 3, 4, 5, 6])
print(myseries)

mycharseries = pd.Series(['a', 'b', 'c', 'd', 'e'])
print(mycharseries) 

# Create series with custom index
myseries = pd.Series([1, 2, 3, 4, 5, 6], index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(myseries)

mycharseries = pd.Series(['a', 'b', 'c', 'd', 'e'], index = ['1', '2', '3', '4', '5'])
print(mycharseries) 