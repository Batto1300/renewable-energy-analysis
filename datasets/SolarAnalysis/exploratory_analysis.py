""" This script imports all the cleaned dataframes 
    and merges them into a single multilevel index dataframe.
"""

import pandas as pd

ENERGY_CAPACITY = "SolarAnalysis/Cleaning/cleaned_all_energy_capacity.csv"
ENERGY_CONSUMPTION = "SolarAnalysis/Cleaning/cleaned_energy_consumption.csv"
MERIDIAN_DISTANCE = "SolarAnalysis/Cleaning/cleaned_meridian_countries.csv"


# group the filenames in a list with a name indentifier
dataframes = {"solar": ENERGY_CAPACITY, "consumption": ENERGY_CONSUMPTION,
              "meridian": MERIDIAN_DISTANCE}

# use a for loop to import all files
for key,value in dataframes.items():
    df = pd.read_csv(value, index_col=['country'])
    dataframes[key] = df

# concatenate on "dataframes" along the columns
# the output is a multi_level index with the key as top level
# the inner join will join on the common row indexes country
DATA = pd.concat(dataframes, axis=1, join="inner")


# u might want to save it elsewhere so as not to repeat the process each time