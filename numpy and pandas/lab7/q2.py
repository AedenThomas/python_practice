
import pandas as pd
import numpy as np

sales = {"Tony": 103, "Sally": 202, "Randy": 380, "Ellen": 101, "Fred": 82}

region = {
    "Tony": "West",
    "Sally": "South",
    "Carl": "West",
    "Archie": "North",
    "Randy": "East",
    "Ellen": "South",
    "Fred": np.nan,
    "Mo": "East",
    "HanWei": np.nan,
}

# a) Create Sales Dataframe and Region Dataframe using above Dictionaries note: pd.DataFrame.from dict()
sales_df = pd.DataFrame.from_dict(sales, orient="index", columns=["sales"])

region_df = pd.DataFrame.from_dict(region, orient="index", columns=["region"])

# b) Write the python command to get the below output:
merged_df = sales_df.merge(region_df, left_index=True, right_index=True)
merged_df = merged_df.fillna("NaN")
print(merged_df)

# c) Write the python command to get the below output:
merged_df = sales_df.merge(region_df, left_index=True, right_index=True)
print(merged_df)

# d)
merged_df = sales_df.merge(region_df, left_index=True, right_index=True)
print(merged_df.groupby("region").sum())

# e)

# f)


# g)
merged_df = sales_df.merge(region_df, left_index=True, right_index=True)
merged_df = merged_df.fillna("NaN")
merged_df["sales_region"] = merged_df["sales"]
merged_df["sales_region"] = merged_df.groupby("region")["sales_region"].transform("sum")
print(merged_df)
