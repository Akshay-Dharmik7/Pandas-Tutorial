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

## Adding New Column in pandas
- In Pandas, a new column can be added to a DataFrame using:
    - Assignment operator (=)
    - insert()

### 1. Add Column Using Assignment (=):
- Most common method.
- Syntax: `df[column_name] = [values]`

#### Important Rule:
- Length of values must match number of rows.

#### Add Column with Single Value:
- Syntax: `df[column_name] = 'value'`

### Add Column Using insert()
- Used to insert column at specific position.
- Syntax: `df.insert(location, column_name, values)`

| Parameter    | Meaning            |
| ------------ | ------------------ |
| `location`   | Position index     |
| `column_name`| Column name        |
| `values`     | Values to insert   |


## Deleting Columns from Dataframe
### df.drop():
- drop() is used to remove:
    - Rows
    - Columns
- from a DataFrame.
- Syntax: `df.drop(labels, axis=0, inplace=False)`

| Parameter      | Meaning          |
| -------------- | ---------------- |
| `labels`       | Row/column name  |
| `axis=0`       | Remove rows      |
| `axis=1`       | Remove columns   |
| `inplace=True` | Permanent change |

### 1. Drop Rows:
- Default axis is 0.
- df2 = df.drop(1)

### 2. Drop Columns
- df.drop(column_name, axis=1)

### 3. Remove Multiple Columns
- df.drop(['Age', 'Marks'], axis=1)


## Updating Data in Dataframe:
### loc[] and iloc[] in pandas
- loc[] and iloc[] are used for:
    - Selecting rows
    - Selecting columns
    - Accessing specific data
    - Updating values
- from a DataFrame.

### loc[] in Pandas
- loc[] works with:
    - Row labels
    - Column names
- Syntax: `df.loc[row_label, column_label]`

### 1. Select Single Row
- df.loc[1]

### 2. Select Multiple Rows
- df.loc[[0,2]]

### 3. Select Specific Columns
- df.loc[:, ['column1', 'column2']]

### 4. Select Rows and Columns Together
- print(df.loc[0:2, ['column1', 'column2']])

### 5. Update Data Using loc[]
df.loc[1, 'column'] = value


### iloc[] in Pandas
- iloc[] works with:
     - Integer positions
- Syntax: `df.iloc[row_position, column_position]`

### 1. Select Single Row
- df.iloc[1]

### 2. Select Multiple Rows
- df.iloc[[0,2]]

### 3. Select Specific Columns
- df.iloc[:, [0,2]]

### 4. Select Rows and Columns Together
- df.iloc[0:3, 0:2]

### 5. Update Data Using iloc[]
- df.iloc[0, 2] = 99

## Handling Missing Values in pandas
- Missing values are empty or unavailable data in a dataset.
- In Pandas, missing values are usually represented as:
    - `NaN`
    - (NaN = Not a Number)

### Why Handle Missing Values?
- Missing values can cause problems in:
    - Data analysis
    - Machine Learning
    - Calculations
    - Visualization
- So they must be:
    - Detected
    - Removed
    - Replaced

### 1. Detect Missing Values
- Using isnull() or isna().

#### a) isnull()
- `df.isnull()`

#### b) isna
- `df.isna`

#### c) Count Missing Values
- `df.isnull().sum()`

### 2. Remove Missing Values
- Using dropna().

#### a) Remove Rows with Missing Values
- `df.dropna()`

#### Remove Columns with Missing Values
- `df.dropna(axis=1)`

| Axis     | Meaning |
| -------- | ------- |
| `axis=0` | Rows    |
| `axis=1` | Columns |


### 3. Fill Missing Values
- Using fillna().

#### a) Fill with Mean
- df['Age'] = df['Age'].fillna(df['Age'].mean())

#### b) Fill with Median
- df['Age'].fillna(df['Age'].median())

#### c) Fill with Mode
- df['Age'].fillna(df['Age'].mode()[0])

### 4. Forward Fill (ffill)
- Uses previous value.
- `df.fillna(method='ffill')`

### 5. Backward Fill (bfill)
- Uses next value.
- `df.fillna(method='bfill')`

### 6. Interpolation
- Fills values mathematically.
- Syntax: `df.interpolate()`

### Interpolation in pandas
- Interpolation is used to fill missing values (NaN) by estimating values based on nearby data.
- It is commonly used in:
    - Time series data
    - Numerical datasets
    - Data preprocessing
    - Machine Learning

#### Why Use Interpolation?
- Instead of removing missing values, interpolation estimates them intelligently.

#### 1. Basic Interpolation
- `df.interpolate()`

#### 2. Linear Interpolation (Default)
- Default method: `df.interpolate(method='linear')`
- Works best for numerical continuous data.

#### 3. Forward Interpolation
- Uses previous value.
- `df.interpolate(method='pad')`

#### 4. Backward Interpolation
- Uses next value.
- `df.interpolate(method='backfill')`

#### 5. Polynomial Interpolation
- Used for curved data patterns.
- `df.interpolate(method='polynomial', order=2)`

#### 6. Time Interpolation
- Used with datetime index.
- `df.interpolate(method='time')`
- Useful for:
    - Stock prices
    - Sensor data
    - Weather data

#### 7. Check Non-Missing Values
- Using notnull().
- `df.notnull()`

## Sorting and Aggregation in pandas
- Sorting and aggregation are important operations in Pandas used for:
    - Organizing data
    - Summarizing data
    - Analyzing datasets
    - Finding patterns and statistics

## 1. Sorting in Pandas
- Sorting means arranging data in:
    - Ascending order
    - Descending order
- Pandas provides:

| Function        | Purpose        |
| --------------- | -------------- |
| `sort_values()` | Sort by values |
| `sort_index()`  | Sort by index  |

### sort_values()
- Sorts rows based on column values.
- Syntax:
    - `df.sort_values(by='column_name')`

### Sort_index()
- Sorts based on row labels.
-  Syntax:
    - `df.sort_index()`

### Important Parameters

| Parameter   | Meaning          |
| ----------- | ---------------- |
| `by`        | Column name      |
| `ascending` | True/False       |
| `inplace`   | Permanent change |


## 2. Aggregation in Pandas
- Aggregation means summarizing data using statistical operations.
- Examples:
    - Sum
    - Average
    - Count
    - Maximum
    - Minimum

### Common Aggregation Functions
| Function   | Purpose            |
| ---------- | ------------------ |
| `sum()`    | Total              |
| `mean()`   | Average            |
| `max()`    | Maximum            |
| `min()`    | Minimum            |
| `count()`  | Count values       |
| `std()`    | Standard deviation |
| `median()` | Middle value       |

### Multiple Aggregations
- Using agg().
- Example:
    - `print(df['Marks'].agg(['sum', 'mean', 'max']))`

### Group-wise Aggregation
- Using groupby(). 









