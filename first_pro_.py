import pandas as pd 
import matplotlib.pyplot as plt 

data = ({ 
    "item" : ["laptop" , "mobile" , "charger" , "ipad" ] ,
    "day" :[1,2,3,4] , 
    "sales" : [ 100, 200 , 400 , 300 ] 
 }) 
df = pd.DataFrame(data) 

plt.plot(df["day"] , df["sales"] , marker = 'o') 

max_sales = df["sales"].max()
max_day = df[df["sales"] == max_sales]["day"].values[0]  

plt.annotate ("Peak",
              xy= (max_day, max_sales),
             xytext=(max_day-2, max_sales+1),
             arrowprops=dict(facecolor='black'))


plt.xlabel("days")
plt.ylabel("sales") 
plt.title("electric sales")
plt.show() 

