""" 
    This script analyses the cleaned dataframes
    on cumulative solar energy capacity, energy 
    consumption and meridian distance from the equator.
    First the the data on cumulative energy capacity
    is filtered for solar energy and saved to a 
    temporary csv file.
    The dataframes are then merged into a single 
    multilevel index dataframe ready for exploratory 
    analysis.
    Note: by storing the dataframes into a dictionary 
    with the key being an identifies, then by 
    applying the pandas concatenate function onto 
    the dataframe, the keys will be the indexes name 
    for the highest level of the multilevel indexed 
    merged dataframe.
"""
import pandas as pd
# import class with full paths to files
import file_names as fn
import os
import numpy as np
import matplotlib.pyplot as plt
import sklearn.cluster
import scipy

# assign paths of the cleaned and/or filtered data sets to a static variable
ALL_ENERGY_CAPACITY = fn.CleanedPaths.CAPACITY
ENERGY_CONSUMPTION = fn.CleanedPaths.CONSUMPTION
MERIDIAN_DISTANCE = fn.CleanedPaths.MERIDIAN
# store filtered dataset for solar capacity in a new csv file
TEMP_SOLAR_ENERGY_CAPACITY = os.path.join(fn._adjusted_path, 'analysis', 'solar_capacity.csv')


# import energy capacity dataset
df_energy_capacity = pd.read_csv(ALL_ENERGY_CAPACITY)
# filter for solar
df_solar_energy_capacity = df_energy_capacity[df_energy_capacity["Technology"] == "Solar"]
# store data in a new file
df_solar_energy_capacity.to_csv(TEMP_SOLAR_ENERGY_CAPACITY)
# group the filenames (values) in a dictionary with a name indentifier (key)
dataframes = {"solar": TEMP_SOLAR_ENERGY_CAPACITY, "consumption": ENERGY_CONSUMPTION,
              "meridian": MERIDIAN_DISTANCE}
# loop over all key,value pairs of the dataframes dictionary
for key, value in dataframes.items():
    # import the csv file into a dataframe & set the country column as index
    df = pd.read_csv(value, index_col=['country'], decimal=",")
    # replace the filename with the respective dataframe
    dataframes[key] = df
# concatenate the "dataframes" along the columns - the output is a multi_level index with the key as top level
data = pd.concat(dataframes, axis=1, join="inner")
# remove temporary file 
os.remove(TEMP_SOLAR_ENERGY_CAPACITY)
# column indexes names: consumption', 'meridian', 'solar'], ['2000'-'2015', 'Technology', 'meridian']

# 1 - WHICH COUNTRY OWN MOST OF THE ELECTRIC CAPACITY SYSTEMS
# cumulative solar energy capacity as of 2015 - string to floats - ascending order
solar_capacity_2015 = data["solar"]["2015"].astype(float).sort_values(ascending = False)
# % total europe solar energy capacity by country - 2015
solar_capacity_2015_percentage = solar_capacity_2015/solar_capacity_2015.sum()*100
# plot a bargraph
solar_capacity_2015_percentage.plot.bar()
# title
plt.title("% Total Europe Solar Energy Capacity 2015")
# ylabel
plt.ylabel("% Solar Capacity")
# show graph
plt.show()
# close window
plt.close("all")
# the top 20% european countries "own" 88% of the cumulative energy capacity in Europe as of 2015

# SOLAR ENERGY CAPACITY VS GEOGRAPHICAL LOCATION/MERIDIAN DISTNACE - resolve graphical issue
solar_capacity_2015 = data["solar"]["2015"].astype(float)
# look at the magnitudes
meridian = data["meridian"]["meridian"].astype(float)
# scatter plot: solar capacity vs meridian distance
plt.scatter(meridian, solar_capacity_2015, alpha=.8, c=range(len(meridian))) # c=range(len(meridian))
# set style
plt.style.use('classic')
plt.grid()
plt.xlabel("Meridian Distance (km)")
plt.ylabel("Cumulative Energy Capacity (M...)")
plt.show()
plt.close("all")

# Not all countries require the same amount of energy throughout the year - different demands
# so we cluster nations in terms of their (cumulative) energy consumption
# we want three groups - low, medium and high consumption levels (put binning function? and say why kmeans is better)
# the following imports and implements a k-means algorithm
#  on our column of interest
# calculate cumulative/total energy consumption 2000 -> 2015
data["consumption", "total"] = data["consumption"].sum(axis = 1)
# cluster countries in 3 groups according to their total energy consumption over the years 2000-2015
kmeans = sklearn.cluster.KMeans(n_clusters=3, random_state=0).fit(
    np.array(data["consumption", "total"]).reshape(-1, 1))
# assign the country's level of consumption attribute in the dataframe
data["consumption", "levels"] = kmeans.labels_
# assign meaning to cluster labels
# plotting energy capacity vs meridian distance for different groups - bad code
levels = [0,1,2]
for i in range(3):
    y = data[data["consumption", "levels"]==i]["solar","2015"].values
    x = data[data["consumption", "levels"]==i]["meridian", "meridian"].values
    plt.scatter(x=list(x.astype(np.float)), y=list(y.astype(np.float)), marker='o', label="low")
    plt.show()
    print(scipy.stats.spearmanr(list(x.astype(np.float)), list(y.astype(np.float))))
plt.close()
"""energy_consumption_groups = {"low": list(datadata.index.values[df["labels"] == 0]),
              "medium":  list(df["country"][df["labels"] == 1]),
              "high": list(df["country"][df["labels"] == 2])}
ax2 = plt.subplot(131)
ax2.plot(meridian[GDP_groups["low"]], total_capacity[GDP_groups["low"]],
         marker='o', linestyle='', ms=8, label="low")
ax2.legend()

ax3 = plt.subplot(132)
ax3.plot(meridian[GDP_groups["medium"]], total_capacity[GDP_groups["medium"]],
         marker='o', linestyle='', ms=8, label="medium")
ax3.grid(True)
ax3.legend()

ax4 = plt.subplot(133)
ax4.plot(meridian[GDP_groups["high"]], total_capacity[GDP_groups["high"]],
         marker='o', linestyle='', ms=8, label="high")
ax4.legend()

plt.show()
plt.close("all")
"""