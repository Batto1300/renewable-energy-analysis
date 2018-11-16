""" This script cleans the original data set 
    containing the energy consumption figures 
    for the world countries.
    Firsly, we remove some redundant rows. 
    Secondly, we filter the dataset for those 
    countries and years which are common to 
    all datasets. 
"""
import pandas as pd 
# import class with full paths to files
import file_names as fn
# original data (csv file) - energy consumption for world countries
ORIGINAL_ENERGY_CONSUMPTION = fn.OriginalPaths.CONSUMPTION
# years and countries common to all datasets
COUNTRIES = fn.CleanedPaths.COUNTRIES
YEARS = fn.CleanedPaths.YEARS
# name of new csv file to store the new cleaned dataset
CLEANED_ENERGY_CONSUMPTION = fn.CleanedPaths.CONSUMPTION


# import the data on energy consumption into a dataframe object
df_energy_consumption = pd.read_csv(ORIGINAL_ENERGY_CONSUMPTION)
# the appropriate header row with the years is in row index 1
header = df_energy_consumption.iloc[1]
# change the first entry of header (= "Million...") to "country"
header[0] = "country"
# change UK to United Kingdom
header = list(map(lambda x: str.replace(x, "UK", "United Kingdom"), header))
# set the new header to the dataframe
df_energy_consumption.columns = header
# drop last 3 columns - simple summary statistics not useful
df_energy_consumption.drop(columns = header[-3:], inplace = True)
# drop first 2 rows - getting the dataframe into the same format as others
df_energy_consumption = df_energy_consumption[3:]
# importing countries and years common to all dataframes
df_countries = pd.read_csv(COUNTRIES)
df_years = pd.read_csv(YEARS)
# from dataframe object to list
years = list(df_years["years"])
# convert years from integer to string type
years = list(map(str, years))
# filter for common countries through merging with countries dataframe
df_energy_consumption = pd.merge(df_energy_consumption, df_countries, on="country", how="inner")
# set country column as index column - this way we can filter for the years
df_energy_consumption.set_index("country", inplace = True)
# filter only for the years commom to all data sets
df_energy_consumption = df_energy_consumption[years]
# save cleaned data set to a new csv file
df_energy_consumption.to_csv(CLEANED_ENERGY_CONSUMPTION)