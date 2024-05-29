import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/content/drive/MyDrive/Historical_Data.csv")

# Example of the data is below
#  	Date 	Article_ID 	Country_Code 	Sold_Units
# 0 	20170817 	1132 	AT 	1.0
# 1 	20170818 	1132 	AT 	1.0
# 2 	20170821 	1132 	AT 	1.0
# 3 	20170822 	1132 	AT 	1.0
# 4 	20170906 	1132 	AT 	1.0

data.info()

data.describe

data.isnull().sum()

print("Unique \n", data['Date'].unique())
print("Value counts \n",data['Date'].value_counts())

x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

d1 = data.iloc[0]
print(d1)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
print(imputer)
imputer.fit(x[:, 0:1])
x[:, 0:1] = imputer.transform(x[:, 0:1])

d=data.Sold_Units.mean()
print(d)

from sklearn. compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [2])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
y

