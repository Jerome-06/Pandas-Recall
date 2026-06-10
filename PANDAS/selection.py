import pandas as pd
df = pd.read_csv("pandas/data.csv",index_col="Name")

#Selection by column
"""
print(df["Name"].to_string())
print(df[["Age"]].to_string())
print(df[["Name","Age"]].to_string())"""

#Selection by row
#print(df.loc["Student_5":"Student_10",["Age","Department"]])

student =input("Enter the name of the student: ")

try:
    print(df.loc[student])
except KeyError:
    print(f"{student} not found in the DataFrame.")