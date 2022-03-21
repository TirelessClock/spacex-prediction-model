import pandas as pd
import requests
import json

BoosterVersion = []
Longitude = []
Latitude = []
LaunchSite = []
PayloadMass = []
Orbit = []
Block = []
ReusedCount = []
Serial = []
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []

def extras_yeet(df):
    for i in range(len(df['rocket'])):
        df['payloads'][i] = str(df['payloads'][i][0])
        df['cores'][i] = str(df['cores'][i][0])    
    df['date'] = pd.to_datetime(df['date_utc']).dt.date

def getBoosterVersion(df):
    c = 0
    print("Loading Booster Data:",end = " ")
    for x in df['rocket']:
        c += 1
        if c%3 == 0:
            print("#", end="")
        response = requests.get("https://api.spacexdata.com/v4/rockets/"+str(x)).json()
        BoosterVersion.append(response['name'])
    print("\nBooster Data Loaded")

def getLaunchSite(df):
    c = 0
    print("\nLoading Launch Data:",end = " ")
    for x in df['launchpad']:
        c += 1
        if c%3 == 0:
            print("#", end="")
        
        response = requests.get("https://api.spacexdata.com/v4/launchpads/"+str(x)).json()
        Longitude.append(response['longitude'])
        Latitude.append(response['latitude'])
        LaunchSite.append(response['name'])
    print("\nLaunch Data Loaded")

def getPayloadData(df):
    c = 0
    print("\nLoading Payload Data:",end = " ")    
    for load in df['payloads']:
        c += 1
        if c%3 == 0:
            print("#", end="")
        response = requests.get("https://api.spacexdata.com/v4/payloads/"+load).json()
        PayloadMass.append(response['mass_kg'])
        Orbit.append(response['orbit'])
    print("\nPayload Data Loaded")

def getCoreData(data):
    c = 0
    print("\nLoading Core Data:",end = " ")
    for core in data['cores']: # here core represents a single row
        
        core = core.replace("\'", "\"")
        core = core.replace("True", "true")
        core = core.replace("False", "false")
        core = core.replace("None", "null")

        core = json.loads(core)

        c += 1
        if c%3 == 0:
            print("#", end="")
        if core['core'] != None:
            response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
            Block.append(response['block'])
            ReusedCount.append(response['reuse_count'])
            Serial.append(response['serial'])
        else:
            Block.append(None)
            ReusedCount.append(None)
            Serial.append(None)
        Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
        Flights.append(core['flight'])
        GridFins.append(core['gridfins'])
        Reused.append(core['reused'])
        Legs.append(core['legs'])
        LandingPad.append(core['landpad'])

def launchDict(data):
    launch_dict = {'FlightNumber': list(data['flight_number']),
    'Date': list(data['date']),
    'BoosterVersion':BoosterVersion,
    'PayloadMass':PayloadMass,
    'Orbit':Orbit,
    'LaunchSite':LaunchSite,
    'Outcome':Outcome,
    'Flights':Flights,
    'GridFins':GridFins,
    'Reused':Reused,
    'Legs':Legs,
    'LandingPad':LandingPad,
    'Block':Block,
    'ReusedCount':ReusedCount,
    'Serial':Serial,
    'Longitude': Longitude,
    'Latitude': Latitude}
    return launch_dict

def csvExport(df):
    landing_outcomes = df.value_counts("Outcome")

    bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])

    landing_class = []

    for i in df["Outcome"]:
        if i in bad_outcomes:
            landing_class.append(1)
        else:
            landing_class.append(0)

    df["Class"] = landing_class

    df.to_csv("dataset.csv", index=False)