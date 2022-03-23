import seaborn as sns
import matplotlib.pyplot as plt  
import pandas as pd 

df = pd.read_csv("dataset.csv")

# Launchsite v Outcome
sns.catplot(y="Outcome", x="LaunchSite", hue="Class", data=df, aspect = 2)
plt.xlabel("LaunchSite",fontsize=20)
plt.ylabel("Outcome",fontsize=20)
# plt.show()
plt.savefig('Graphs/LaunchSite_v_Outcome.png')

# FlightNumber v PayloadMass
print("A")
sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 2)
print("A")
plt.xlabel("FlightNumber",fontsize=20)
print("A")
plt.ylabel("PayloadMass",fontsize=20)
# plt.show()
print("A")
plt.savefig('Graphs/PayloadMass_v_FlightNumber.png')
