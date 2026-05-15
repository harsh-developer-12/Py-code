import pandas as pd
import matplotlib.pyplot as plt 


data = {
    "Captain": ["Dhoni", "Dhoni", "Dhoni","Kohli", "Kohli", "Kohli", "rohit", "rohit", "rohit"],

    "Format": ["Test", "ODI", "T20","Test", "ODI", "T20","Test", "ODI", "T20"],

    "Matches": [60, 200, 72, 68, 95, 50,77, 230, 17],

    "Wins": [27, 110, 41,40, 65, 30,48, 165, 10],

    "Losses": [18, 74, 28,17, 27, 16,16, 51, 5]
}

df = pd.DataFrame(data)


df["Win %"] = (df["Wins"] / df["Matches"]) * 100

df["Loss %"] = (df["Losses"] / df["Matches"]) * 100 

print(df[df["Captain"] == "Dhoni"][["Captain" ,"Format" ,"Matches" , "Win %" , "Loss %"]]) 

print(df[df["Captain"] == "rohit"][["Captain","Format" , "Matches" , "Win %" , "Loss %"]])

print(df[df["Captain"] == "Kohli"][["Format" , "Matches" , "Win %" , "Loss %"]])

# fig, ax1 = plt.subplots()

# for captain in df["Captain"].unique():
#     temp = df[df["Captain"] == captain] 

cap = df.groupby("Captain")["Wins"].sum()

plt.pie (
    cap , 
    labels= cap.index,
    autopct="%1.1f%%",
    explode=[0.05,0.05,0.05],
    startangle=90    

)

    # ax1.pie(temp["Format"], temp["Win %"],marker='o', label=captain)

# ax1.set_xlabel("Format")
# ax1.set_ylabel("Win %")
# ax1.set_title("Win % Comparison")
# ax1.legend()

plt.show()


