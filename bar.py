import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Captain": ["Dhoni","Dhoni","Dhoni",
                "Kohli","Kohli","Kohli",
                "Ponting","Ponting","Ponting"],

    "Format": ["Test","ODI","T20",
               "Test","ODI","T20",
               "Test","ODI","T20"],

    "Wins": [27,110,41,
             40,65,30,
             48,165,10]
}


df = pd.DataFrame(data)


# groupby
summary = df.groupby(["Captain" , "Format"])["Wins"].sum().unstack()

# plot
summary.plot(kind="bar", title="Total Wins by Captain")

plt.xlabel("Captain")
plt.ylabel("Wins")
plt.show()  

