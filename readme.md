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