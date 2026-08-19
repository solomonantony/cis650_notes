# About pandas
- One of the most popular Python packages is pandas
- pandas provides great tools for collecting, transforming, and analyzing tabular data
-- Example: from a sales transaction database, with pandas you can…
- Read the specific database records of interest
- Filter out incorrect data
- Summarize the data according to different dimensions
-- E.g., product type, regions, time period
- Display different type of charts to visualize the results
- … in very few lines of code

- Tables are a common way to organize data
- Python does not have a built-in table structure
- You can use lists of lists, or dictionaries
- But these don't have a natural row/column orientation
## pandas provides:
- The DataFrame type – load, store, transform, process tabular data
- The Series type – a list of items, each of which is named
- pandas provides more than 200 functions and methods
- With these, you can write concise, efficient, powerful code
## Dataframe structure
- DataFrame is a matrix of data; Enhanced two-dimensional array
- Each column and row has a name (a.k.a indices)
- The set of row names is called the index
- Within a given column, the cells generally have the same data type
- For numbers, pandas uses NumPy package types
- More efficient in speed and memory than Python types
- a DataFrame cell can contain any Python data type
- Support missing data
- Each column in a DataFrame is a Series
## using pandas
- In order to use pandas (and other 3rd-party Python packages), you need to - install the package on your computer or Python environment
- In addition, your program needs to load the package into memory by using the - Python import statement
- A common way to do this for pandas is:
- import pandas as pd
- The above statement indicates:
- We'd like to use the pandas package
- We'll use an alternative name, in this case pd, when referring to items in the package
