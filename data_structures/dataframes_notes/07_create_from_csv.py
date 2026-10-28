import pandas as pd

# Read the CSV into a DataFrame
df = pd.read_csv("data_structures\\dataframes_notes\\accounts.csv", names=["account", "name", "balance"])

# Look at the data
print(df)
print(df.dtypes)                  # data type of each column
print(df["balance"].sum())   
