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
    df = pd.read_csv(value, index_col=['country'])
    # replace the filename with the respective dataframe
    dataframes[key] = df

# concatenate the "dataframes" along the columns
DATA = pd.concat(dataframes, axis=1, join="inner")
# the output is a multi_level index with the key as top level
# the inner join will join on the common row indexes country
# we're ready for exploratory analysis
