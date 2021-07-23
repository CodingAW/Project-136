import csv
import pandas as pd

df = pd.read_csv("filteredStar.csv")

df.drop(["Unnamed: 0"], axis= 1, inplace= True)
df.drop(["Unnamed: 0.1"], axis= 1, inplace= True)

finalDict = []
name = df["Star_name"].tolist()
distance = df["Distance"].tolist()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

temp_dict = {}

for i in range(0, len(name)):
    temp_dict["name"] = name[i]
    temp_dict["mass"] = mass[i]
    temp_dict["distance"] = distance[i]
    temp_dict["radius"] = radius[i]
    temp_dict["gravity"] = gravity[i]

    finalDict.append(temp_dict)
    temp_dict = {}

print(finalDict)