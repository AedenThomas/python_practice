# Question3:
# Create a dataframe for the following data:
# Date
# 0 2021-10-01 1014.0
# 1 2021-10-02 1014.0
# 2 2021-10-03
# NaN
# 3 2021-10-04 1014.0
# 4 2021-10-05 1014.0
# 5 2021-10-06 1014.0
# 6 2021-10-07 1014.0
# 7 2021-10-08 1014.0
# 8 2021-10-09 1014.0
# 9 2021-10-10
# NaN
# Item Measure_1 Measure_2 Measure_3 Measure_
# 8.0
# 1.0
# NaN
# 3.0
# 5.0
# 6.0
# 8.0
# NaN
# 1.0
# NaN
# 0.53
# 0.84
# NaN
# NaN
# 0.08
# 0.94
# 0.17
# 0.45
# 0.44
# 0.01
# 0.79
# 0.16
# NaN
# 0.26
# 0.91
# 0.64
# 0.60
# NaN
# NaN
# NaN
# NaN
# NaN
# NaN
# NaN
# 0.00
# -1.000761
# 0.72
# -1.871924
# 0.39
# 1.745967
# Try the following options:
# 1. Drop rows or columns that have a missing value
# 2. Drop columns that have at least one missing value by using the axis parameter=1
# 3. Drop rows or columns that only have missing values
# 4. Drop rows or columns based on a threshold value 3 or more NAN
# 5. Replace NaN with the previous value
# 6. Replace NaN with the previous value with limit=1
# 7. Replace NaN with the forward value


import pandas as pd
import numpy as np


# creating a dataframe
df = pd.DataFrame(
    {
        "Date": pd.date_range("2021-10-01", periods=10),
        "Item": [
            1014.0,
            1014.0,
            np.nan,
            1014.0,
            1014.0,
            1014.0,
            1014.0,
            1014.0,
            1014.0,
            np.nan,
        ],
        "Measure_1": [8.0, 1.0, np.nan, 3.0, 5.0, 6.0, 8.0, np.nan, 1.0, np.nan],
        "Measure_2": [0.53, 0.84, np.nan, np.nan, 0.08, 0.94, 0.17, 0.45, 0.44, 0.01],
        "Measure_3": [
            0.79,
            0.16,
            np.nan,
            0.26,
            0.91,
            0.64,
            0.60,
            np.nan,
            np.nan,
            np.nan,
        ],
        "Measure_4": [
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            0.00,
            -1.000761,
            0.72,
        ],
    }
)

# 1. Drop rows or columns that have a missing value
print(df.dropna())

# 2. Drop columns that have at least one missing value by using the axis parameter=1
print(df.dropna(axis=1))

# 3. Drop rows or columns that only have missing values
print(df.dropna(how="all"))

# 4. Drop rows or columns based on a threshold value 3 or more NAN
print(df.dropna(thresh=3))

# 5. Replace NaN with the previous value
print(df.fillna(method="ffill"))

# 6. Replace NaN with the previous value with limit=1
print(df.fillna(method="ffill", limit=1))

# 7. Replace NaN with the forward value
print(df.fillna(method="bfill"))
