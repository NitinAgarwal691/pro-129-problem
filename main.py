import pandas as pd 
import csv 
df=pd.read_csv("dwarf_stars.csv")
df=df.dropna()
# for i in enumerate(df):
df['Mass'] = df['Mass'].astype(float)
df['Radius'] = df['Radius'].astype(float)
df['Radius']= df['Radius']*0.102763
df['Mass']=df['Mass']*0.000954588
df.to_csv('main.csv')
print(df.shape)