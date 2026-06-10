import pandas as pd
data={"Name":["John","Anna","Peter","Linda"],
      "Age":[28,24,35,32]} 

df=pd.DataFrame(data,index=['a','b','c','d'])
print(df.loc['c'])

print(df[df['Age']>30])
df["Job"]=["Engineer","Doctor","Artist","Lawyer"]
print(df)
 
 #ADD new Rows 
new_row=pd.DataFrame({"Name":"Tom","Age":30,"Job":"Teacher"},{"Name":"rar","Age":30,"Job":"Teacher"}, index=['e','f']) 
df=pd.concat([df,new_row] )
print(df)