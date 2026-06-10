import pandas as pd
#csv file
df = pd.read_csv("pandas/data.csv")
print(df.to_string())

#json file
df = pd.read_json("data.json")
print(df.to_string())