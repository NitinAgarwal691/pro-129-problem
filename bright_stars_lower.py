import csv
import pandas as pd 
data=[]
with open("bright_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for rows in csvreader:
        data.append(rows)

header=data[0]
planet_data=data[1:]

for lower_planet_data in planet_data:
    lower_planet_data[1]=lower_planet_data[1].lower()

planet_data.sort(key=lambda planet_data:planet_data[1])

with open("bright_stars.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)