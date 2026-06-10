import pandas as pd

#Aggregation = Reduses a set of value into a single summary value 
#            Used to summarize and analyze data
#            Often used with groupby() function  

df=pd.read_csv("pandas/data.csv")

#Whole DataFrame
"""
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())
"""
#Single Column
"""
print(df["Score"].mean())
print(df["Score"].sum())
print(df["Score"].min())
print(df["Score"].max())
print(df["Score"].count())
"""
#GroupBy
"""
group = df.groupby("Department")
print(group["Score"].mean())
print(group["Score"].sum())
print(group["Score"].min())
print(group["Score"].max()) 
"""




