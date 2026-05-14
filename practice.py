import pandas as pd  

data = {
    "name" : ["ayus" , "ramu" , "monu" , "golu"  ],
        "age" : [24 , 26 , None , 23 ] , 
        "dipart" : ["emply" , "emply" , "hr" , "fresh" ]
} 

df = pd.DataFrame(data) 
# print(df) 

for i ,row in df.iterrows():
    print(i,row["name"] , row["age"] , row["dipart"])


# df.to_csv("practis.csv" , index=False) 

