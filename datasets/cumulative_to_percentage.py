import pandas as pd 
import os

FILENAME = "all-energy-capacity-eu-adj.csv"

# reads and converts the csv file into a datafreame 
df = pd.read_csv(FILENAME, skiprows = 0, index_col = [0,1]) 

# The electricity capacity is cumulative, so we call the function .pct_change to calculate the 
# percentage change from one year to the other 
df.loc[: , "2000":"2017"] = df.loc[: , "2000":"2017"].pct_change(axis = "columns")

os.remove(FILENAME)
df.to_csv(FILENAME)