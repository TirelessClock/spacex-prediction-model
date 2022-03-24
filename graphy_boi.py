import seaborn as sns
import matplotlib.pyplot as plt  
import pandas as pd 

df = pd.read_csv("dataset.csv")

def Extract_year(df):
    year = []
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year

years = Extract_year(df)

# Launchsite v Outcome
sns.catplot(y="Outcome", x="LaunchSite", hue="Class", data=df, aspect = 2)
plt.xlabel("LaunchSite",fontsize=20)
plt.ylabel("Outcome",fontsize=20)
# plt.show()
plt.savefig('Graphs/LaunchSite_v_Outcome.png')

# FlightNumber v PayloadMass
sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 2)
plt.xlabel("FlightNumber",fontsize=20)
plt.ylabel("PayloadMass",fontsize=20)
# plt.show()
plt.savefig('Graphs/PayloadMass_v_FlightNumber.png')

# Yearly Trends
sns.catplot(y = "PayloadMass", x = years, hue = "Class", data = df, aspect = 2)
plt.xlabel("Year", fontsize = 20)
plt.ylabel("PayloadMass", fontsize = 20)
plt.savefig('Graphs/PayloadMass_v_Year.png')

