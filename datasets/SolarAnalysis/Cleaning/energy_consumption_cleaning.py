""" This script cleans the original data set 
    containing the energy consumption figures 
    for the world countries.
    Firsly, we remove some redundant rows. 
    Secondly, we filter the dataset for those 
    countries and years which are common to 
    all datasets. 
"""


import pandas as pd 

# original data (csv file) - energy consumption for world countries
ENERGY_CONSUMPTION = "SolarAnalysis/Cleaning/original/energy_consumption.csv"

# years and countries common to all datasets
COUNTRIES_YEARS = "SolarAnalysis/Cleaning/original/common_countries_and_years.csv"

# # name of new csv file to store the new filtered dataset
OUTPUT_FILENAME = "SolarAnalysis/Cleaning/cleaned_energy_consumption.csv"


# import the data on energy consumption into a dataframe object
df_energy_consumption = pd.read_csv(ENERGY_CONSUMPTION)
# the appropriate header row with the years is in row index 1
header = df_energy_consumption.iloc[1]
# change the first entry of header (= "Million...") to "country"
header[0] = "country"
# set the new header to the dataframe
df_energy_consumption.columns = header
# drop last 3 columns - simple summary statistics not useful
df_energy_consumption.drop(columns = header[-3:], inplace = True)
# drop first 2 rows - getting the dataframe into the same format as others
df_energy_consumption = df_energy_consumption[3:]

# importing countries and years common to all dataframes
df_COUNTRIES = pd.read_csv(COUNTRIES_YEARS, usecols=["country"])
df_years = pd.read_csv(COUNTRIES_YEARS, usecols=["year"])
# # from dataframe object to list
YEARS = list(df_years["year"])
# # convert years from integer to string type
YEARS = list(map(str, YEARS))

# filter for common countries through merging with countries dataframe
df_energy_consumption = pd.merge(df_energy_consumption, df_COUNTRIES, on="country", how="inner")
# set country column as index column - this way we can filter for the years
df_energy_consumption.set_index("country", inplace = True)
# filter only for the years commom to all data sets
df_energy_consumption = df_energy_consumption[YEARS]

# save filtered data set to a new csv file
df_energy_consumption.to_csv(OUTPUT_FILENAME)