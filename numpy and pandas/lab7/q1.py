import pandas as pd
import numpy as np

# dataframe1
df1 = pd.DataFrame({'Name': ['Pankaj', 'Meghna', 'Lisa'], 'Country': ['India', 'India', 'USA'], 'Role': ['CEO', 'CTO', 'CTO']})

# dataframe2
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Pankaj', 'Anupam', 'Amit']})

# merge
df3 = pd.merge(df1, df2, on='Name')
print(df3)

# left join
df4 = pd.merge(df1, df2, on='Name', how='left')
print(df4)

# right join
df5 = pd.merge(df1, df2, on='Name', how='right')
print(df5)

# outer join
df6 = pd.merge(df1, df2, on='Name', how='outer')
print(df6)


