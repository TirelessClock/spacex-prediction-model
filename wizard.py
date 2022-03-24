import os
import house_elf as he
import requests
import pandas as pd
pd.options.mode.chained_assignment = None

url = "https://api.spacexdata.com/v4/launches/past"
response = requests.get(url).json()
df = pd.json_normalize(response)
df = df[['rocket', 'payloads', 'launchpad', 'cores','flight_number', 'date_utc']]
if os.path.exists("dataset.csv") == False:
    he.extras_yeet(df)
    he.getBoosterVersion(df)
    he.getLaunchSite(df)
    he.getPayloadData(df)
    he.getCoreData(df)
    launch_dict = he.launchDict(df)
    df = pd.DataFrame(launch_dict)
    he.csvExport(df)


df = pd.read_csv("dataset.csv")

df = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]

he.OneHotEncoding(df,"Orbit")
he.OneHotEncoding(df,"LaunchSite")
he.OneHotEncoding(df,"LandingPad")
he.OneHotEncoding(df,"Serial")
he.OneHotEncoding(df, "GridFins")
he.OneHotEncoding(df, "Reused")
he.OneHotEncoding(df, "Legs")

df = df.drop(["Orbit", "LaunchSite", "LandingPad", "Serial","GridFins","Reused","Legs"], inplace= False, axis = 1)


he.removeNulls(df, "PayloadMass")
he.removeNulls(df, "Block")

df.astype("float64")
df.to_csv("dataset2.csv")
