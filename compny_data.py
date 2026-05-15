import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame({
    "Order_ID": [1,2,3,4,5,6],
    "Product": ["Laptop","Mobile","Laptop","Tablet","Mobile","Laptop"],
    "City": ["Delhi","Mumbai","Delhi","Delhi","Mumbai","Delhi"],
    "Sales": [50000,20000,55000,15000,25000,60000],
    "Date": ["2024-01-01","2024-01-05","2024-02-10","2024-02-15","2024-03-01","2024-03-10"]
}) 

df.groupby("Product")["Sales"].sum().plot(kind='bar') 


plt.show() 

