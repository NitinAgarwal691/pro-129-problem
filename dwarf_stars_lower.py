import csv
data=[]
with open("dwarf_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for rows in csvreader:
        data.append(rows)

headers=data[0]
planet_data=data[1:]
for data_point in planet_data:
    data_point[1]=data_point[1].lower()

planet_data.sort(key=lambda planet_data:planet_data[1])
with open("dwarf_stars.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)