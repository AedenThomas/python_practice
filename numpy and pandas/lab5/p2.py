import pandas as pd

df=pd.read_csv('/Users/aeden/Developer/python/APP/numpy/gapminder.tsv', sep='\t')

print('df.head()')
print(df.head())

print('df.info()')
print(df.info())

country_df=df['country']
print('country_df.head()')
print(country_df.head())

subset=df[['country', 'continent', 'year']]
print(subset.head())

# loc and iloc
print('loc')
print(df.loc[0])
# print(df.loc[-1]) # error 

print('iloc')
print(df.iloc[0])
print(df.iloc[-1]) # error


# To print last row
no_of_rows=df.shape[0]
print(df.loc[no_of_rows-1])

print(df.head(n=10)) # print first 10 rows

print(df.tail(n=10)) # print last 10 rows

subset_loc=df.loc[0]
subset_head=df.head(n=1)

print(subset_loc)
print(subset_head)

print(df.loc[[0,99,999]])

subset=df.loc[:,['year','pop']] # all rows and year and pop columns
print(subset.head())

subset=df.iloc[:,[2,4,-1]] # all rows and year and pop columns
print(subset.head())

small_range=list(range(5))
print(small_range)

subset=df.iloc[:,small_range]
print(subset.head())



print(df.loc[[42, 0]])
print(df.loc[42, df.columns[0]])

