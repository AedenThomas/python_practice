import numpy as np
import pandas as pd

# Read CSV file into a dataframe
df = pd.read_csv("file.csv")

# Display the index and columns
print("Index and Columns:")
print(df.index)
print(df.columns)

# Modify the labels 101 to 107 to 10 to 17
df.index = np.arange(10, 18)

# Modify the data type of py-score
df["py-score"] = df["py-score"].astype(int)

# Display the shape, size, and number of dimensions
print("Shape:", df.shape)
print("Size:", df.size)
print("Number of dimensions:", df.ndim)

# Implement NumPy slicing of array to get the desired output
print("\nNumPy Slicing:")
print(df.iloc[2:5, 0:3])
