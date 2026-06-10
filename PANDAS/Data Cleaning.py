import pandas as pd

#Data Cleaning = Process of fixing or removing 
#                incorrect, corrupted, incorrectly formatted,
#                duplicate, or incomplete data within a dataset.
#                75% of work done with pandas is data cleaning

df= pd.read_csv("pandas/data.csv")

#1.Drop irrelevant columns
#df=df.drop(columns=["Name", "Age"])

#2.Handle missing data
#df =df.dropna(subset=["Score"]) #drop rows with missing values in the "Score" column
#df =df.fillna({"Score":"none"}) #fill missing values in the "Score" column with "none"

#3.Fix inconsistent data
df["Department"]=df["Department"].replace({"Mech":"Mechanical", "ECE":"Electronics"})

#4. Standardize text
df["Department"]=df["Department"].str.lower() #convert all text in the "Department" column to lowercase
 
#5. Fix data types
df["Score"]=pd.to_numeric(df["Score"], errors="coerce") #convert the "Score" column to numeric, setting invalid parsing to NaN      

#6. remove duplicates
df=df.drop_duplicates() #remove duplicate rows from the DataFrame   
print(df)