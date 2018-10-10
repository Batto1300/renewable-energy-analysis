import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
""" Aim is to investigate whether countries close to the equator have an average solar growth investment larger
than countries further away from the equator """

CAPACITY = "all_energy_capacity_eu_percentage.csv"
GEOPOSITION = "latitude-countries.csv"
 
df_1 = pd.read_csv(CAPACITY, index_col= [0,1])
df_2 = pd.read_csv(GEOPOSITION)
df_1.replace([np.inf, -np.inf], np.nan, inplace = True)


latitude = pd.Series(list(df_2["latitude"]), index = df_2["country"])
average_growth = pd.Series(list(pd.to_numeric(df_1.loc[i].loc["Solar", "2001":"2017"], errors='coerce').mean() for i in list(df_1.index.levels[0]) if i not in ["Europe", "European Union"]), index = [i for i in list(df_1.index.levels[0]) if i not in ["Europe", "European Union"]]  )
#print(df_2.head())
#print(latitude)
#print(df_1.index.levels[0])
#print(pd.to_numeric(df_1.loc["Albania"].loc["Solar", "2001":"2017"], errors='coerce').mean())
print(average_growth)


plt.scatter(latitude, average_growth)
plt.show()


