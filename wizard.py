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

print("A")
df = pd.read_csv("dataset.csv")

he.OneHotEncoding(df,"Orbit")
he.OneHotEncoding(df,"LaunchSite")
he.OneHotEncoding(df,"LandingPad")
he.OneHotEncoding(df,"Serial")

df.to_csv("dataset.csv")
