import pandas as pd 

d = pd.read_csv("practis.cvs") 
# check information of file ye first step 
# print(d.info())     

#second step 
# print(d.describe()) 

#  check null value 
# print(d.isnull().sum())  

# row delete 
# print(d.dropna()) 

#  column delete
# print(d.dropna(axis=1))   

# used for fill value 
# print(d.fillna("0"))   

# index reset 
# print(d.reset_index(drop= True , inplace= True)) 


# d["status"] = "junior" 
# d.loc[d["age"]  < 25 , "status" ]  = "sinior"
# print(d) 


for i , row in d.itterrow() :
    print(row["name"] , row["age"]) 

    