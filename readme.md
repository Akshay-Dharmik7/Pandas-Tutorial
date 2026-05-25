# Pandas Tutorial

### What is Pandas?
- Pandas is a Python library used for working with data sets.
- It has functions for analyzing, cleaning, exploring, and manipulating data.
- The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

### Simple Interview Definition
- Pandas is a powerful Python library used for data manipulation, analysis, cleaning, and handling structured datasets using Series and DataFrame objects.

### Why Use Pandas?
- Pandas allows us to analyze big data and make conclusions based on statistical theories.
- Pandas can clean messy data sets, and make them readable and relevant.
- Relevant data is very important in data science.

### What Can Pandas Do?
- Pandas gives you answers about the data. Like:
    - Is there a correlation between two or more columns?
    - What is average value?
    - Max value?
    - Min value?
- Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

## Pandas Getting Started
### Installation of Pandas
- If you have Python and PIP already installed on a system, then installation of Pandas is very easy.
- Install it using this command:
    - `C:\Users\Your Name>pip install pandas`

### Import Pandas
- Once Pandas is installed, import it in your applications by adding the import keyword:
    - `import pandas`
- Now Pandas is imported and ready to use.

### Example:
import pandas ps pd  

myseries = [1, 2, 3, 4, 5, 6]  
myvar1 = pd.Series(myseries) 
print(myvar1)   

mydataset = {  
  'cars': ["BMW", "Volvo", "Ford"],  
  'passings': [3, 7, 2]  
}  

myvar2 = pd.DataFrame(mydataset)  
print(myvar2)  

## Series in Pandas
### What is a Series?
- A Pandas Series is like a column in a table.
- It is a one-dimensional array holding data of any type.
- A Series is similar to: `NumPy array + Labels(Index)`.


#### Syntax:
- `pd.Series(data, index)`

| Parameter | Description       |
| --------- | ----------------- |
| `data`    | Values            |
| `index`   | Labels (optional) |


#### Example:
s = pd.Series([10, 20, 30, 40])  
print(s)  

### Labels:
- If nothing else is specified, the values are labeled with their index number.
- First value has index 0, second value has index 1 etc.
- This label can be used to access a specified value.

#### Example:
- Return the first value of the Series:
- `print(myvar[0])`.

### Create Series with specific index/label
#### Example:
a = [1, 7, 2]  
myvar = pd.Series(a, index = ["x", "y", "z"])  
print(myvar)  


## DataFrame in pandas
- A DataFrame is a two-dimensional labeled data structure in Pandas.
- It looks like a table with:
    - Rows
    - Columns
    - Indexes
- A DataFrame can store:
    - Numbers
    - Strings
    - Boolean values
    - Mixed data types

### Simple Interview Definition: 
- A DataFrame in Pandas is a two-dimensional labeled data structure used to store and manipulate tabular data with rows and columns.

### Structure of DataFrame
#### Example:
| Index | Name   | Age | City   |
| ----- | ------ | --- | ------ |
| 0     | Akshay | 25  | Pune   |
| 1     | Rahul  | 24  | Mumbai |


## head() and tail() in pandas
- head() and tail() are used to quickly view data in a DataFrame or Series.
- They are very useful for:
    - Checking dataset structure
    - Verifying imported data
    - Inspecting rows

### 1. head() Function:
- head() returns the first rows of a dataset.
- Syntax
    - `df.head(n)`

| Parameter | Description                                |
| --------- | ------------------------------------------ |
| `n`       | Number of rows to display. Default: 5 rows |

### 2. tail() Function:
- tail() returns the last rows of a dataset.
- Syntax:
    - `df.tail(n)`

### Simple Interview Definition
- head() and tail() in Pandas are used to display the first and last rows of a DataFrame or Series for quick data inspection.

## info() in pandas
- info() is used to get a summary of a DataFrame.
- It provides important information like:
    - Number of rows and columns
    - Column names
    - Data types
    - Non-null values
    - Memory usage

- Syntax:
    - `df.info()`

### Simple Interview Definition
- info() in Pandas is used to display a concise summary of a DataFrame, including column names, datatypes, non-null values, and memory usage.


