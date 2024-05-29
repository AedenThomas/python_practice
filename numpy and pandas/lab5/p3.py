import pandas as pd

df=pd.read_csv('/Users/aeden/Developer/python/APP/numpy and pandas/scientists.csv')

ages=df['Age']
print(ages.mean())
print(ages.std())
print(ages[ages>ages.mean()])