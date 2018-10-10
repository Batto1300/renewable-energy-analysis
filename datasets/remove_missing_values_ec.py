import pandas as pd
import os

FILENAME = "all_energy_capacity.csv"

# reads and converts the csv file into a datafreame 
df = pd.read_csv(FILENAME, skiprows = 0, index_col = [0,1]) 

# Remove all countries which contain all missing vales in all energy resources
for i in df.index.levels[0]:   # list of countries, type = string
    if pd.isnull(df.loc[i, "2000" : "2017"]).all().all():
        df.drop(i, inplace = True)

os.remove(FILENAME)
df.to_csv(FILENAME)

