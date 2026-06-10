import pandas as pd
df= pd.read_csv("pandas/data.csv")

#Filtering = Keeping the rows that match a condition and discarding the rest
#mark_student=df[df["Score"]>=75]

#age_student=df[df["Age"]>20]

#dep_student=df[(df["Department"]=="Mech") | (df["Age"]>=20)]

s_studennt=df[(df["Score"]>=75) & (df["Age"]>20)]
print(s_studennt)