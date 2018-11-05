""" This script imports all the cleaned dataframes
    on cumulative energy capacity, energy consumption
    and meridian distance from the equator.
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

# assign the names of the cleaned data sets to a variable
ENERGY_CAPACITY = "SolarAnalysis/Cleaning/cleaned_all_energy_capacity.csv"
ENERGY_CONSUMPTION = "SolarAnalysis/Cleaning/cleaned_energy_consumption.csv"
MERIDIAN_DISTANCE = "SolarAnalysis/Cleaning/cleaned_meridian_countries.csv"


# group the filenames (values) in a dictionary with a name indentifier (key)
dataframes = {"solar": ENERGY_CAPACITY, "consumption": ENERGY_CONSUMPTION,
              "meridian": MERIDIAN_DISTANCE}

# loop over all key,value pairs of the dataframes dictionary
for key,value in dataframes.items():
    # import the csv file into a dataframe & set the country column as index
    df = pd.read_csv(value, index_col=['country'], decimal=",")
    # replace the filename with the respective dataframe
    dataframes[key] = df

# concatenate the "dataframes" along the columns
DATA = pd.concat(dataframes, axis=1, join="inner")
# the output is a multi_level index with the key as top level
# the inner join will join on the common row indexes country
# we're ready for exploratory analysis

import numpy as np
import matplotlib.pyplot as plt

# column indexes names: 
# consumption', 'meridian', 'solar'], ['2000'-'2015', 'Technology', 'meridian']


# cumulative solar energy capacity as of 2015
solar_15 = pd.Series(DATA["solar"]["2015"].astype(float).sort_values(ascending = False))
solar_15 = solar_15/solar_15.sum()
# the top 20% european countries OWN 88% of the cumulative energy capacity as of 2015
solar_15.plot.bar() 

plt.show()
plt.close("all")

# energy capacity as a function of geographical location - closer to equator, higher potential
solar_15 = pd.Series(DATA["solar"]["2015"].astype(float))
# look at the magnitudes
meridian = pd.Series(DATA["meridian"]["meridian"]).astype(float)

plt.scatter(meridian, solar_15, alpha=.4, c=range(len(meridian))) # c=range(len(meridian))
#plt.colorbar()
plt.style.use('classic')
plt.grid()
plt.xlabel("Meridian Distance (km)")
plt.ylabel("Cumulative Energy Capacity (M...)")
plt.show()
plt.close("all")
# not all countries require the same energy production - different demands
