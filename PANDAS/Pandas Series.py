import pandas as pd

"""
data=[100,101,102,103,104]

series=pd.Series(data,index=['j','e','r','o','m'])

print(series.loc['r']) 

series.loc['r']=45
print(series )

print(series.iloc[2])

print(series[series>=103 ])
"""
calories= {"day1":420,"day2":380,"day3":390}
calories_series=pd.Series(calories)

calories_series.loc['day2']+=380
print(calories_series[calories_series>600])