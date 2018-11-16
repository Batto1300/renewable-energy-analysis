""" This script cleans the original data set 
    containing the latitude distance.
    Firsly, we filter the dataset for those 
    countries which are common to all datasets. 
    Secondly, just as a data manipulation exercise, 
    we convert the latitude figures from degrees to 
    kilometres (meridian distance).
    The analysis does not change, however the units of
    measure are more informative.
"""
import pandas as pd
import math
# import class with full paths to files
import file_names as fn


# original data (csv file) - countries latitude
ORIGINAL_LATITUDE = fn.OriginalPaths.LATITUDE
# countries common to all datasets
COUNTRIES = fn.CleanedPaths.COUNTRIES
# save transformed dataframe to new file - meridian distance km
CLEANED_MERIDIAN = fn.CleanedPaths.MERIDIAN


# import only countries and their latitude from the LATITUDE file
df_latitude = pd.read_csv(ORIGINAL_LATITUDE, usecols=["country", "latitude"])
# import the list of countries common to all dataframes
df_countries = pd.read_csv(COUNTRIES)
# filter the dataframe for common countries with merge method
df_latitude = pd.merge(df_latitude, df_countries, on="country", how="inner")
# average earth radius (km)
earth_radius = 6371
# convert latitude distance (degrees) to merdian distance (km)
df_latitude["latitude"] = ((df_latitude["latitude"] * math.pi)/180) * earth_radius
# change name "latitude" to "meridian"
df_latitude.rename(columns = {"latitude":"meridian"}, inplace = True)
# set country to be column index to avoid extra column of row indeces
df_latitude.set_index("country", inplace = True)
# save new dataframe to CLEANED_MERIDIAN
df_latitude.to_csv(CLEANED_MERIDIAN)
