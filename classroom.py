import pandas as pd 

df = pd.read_csv("dataset.csv")


orbit_ohe = pd.get_dummies(df["Orbit"])
for i in orbit_ohe.columns:
    df["Orbit_"+i] = orbit_ohe[i]

ls_ohe = pd.get_dummies(df["LaunchSite"])
for i in ls_ohe.columns:
    df["LaunchSite_"+i] = ls_ohe[i]

lp_ohe = pd.get_dummies(df["LandingPad"])
for i in lp_ohe.columns:
    df["LandingPad_"+i] = lp_ohe[i]

serial_ohe = pd.get_dummies(df["Serial"])
for i in serial_ohe.columns:
    df["Serial_"+i] = serial_ohe[i]

df.to_csv("dataset_2.csv")
