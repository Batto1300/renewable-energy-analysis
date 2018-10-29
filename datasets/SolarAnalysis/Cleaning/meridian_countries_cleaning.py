import pandas as pd
import math

# import original data on countries latitude
LATITUDE = "SolarAnalysis/Cleaning/original/latitude-countries.csv"
# import list of countries common to all dataframes
COMMOM_COUNTRIES = "SolarAnalysis/Cleaning/original/common_countries_and_years.csv"

# save transformed dataframe to new file - meridian distance km
OUTPUT_FILENAME = "SolarAnalysis/Cleaning/cleaned_meridian_countries.csv"

# import countries and their latitude from the CSV file
df_latitude = pd.read_csv(LATITUDE, usecols=["country", "latitude"])
# import the list of countries common to all dataframes
df_countries = pd.read_csv(COMMOM_COUNTRIES, usecols=["country"])
# merger the two dataframes to get only the latitudes for the common countries
df_latitude = pd.merge(df_latitude, df_countries, on="country", how="inner")

""" Following we will convert latitude to meridian distance (km).
    Note that this is not necessary, it won't change th eoutcome 
    of the results. However, I thought it would be a good 
    exercise.  """

# average earth radius (km)
earth_radius = 6371
# convert latitude distance (degrees) to merdian distance (km)
df_latitude["latitude"] = ((df_latitude["latitude"] * math.pi)/180) * earth_radius
# change name "latitude" to "meridian"
df_latitude.rename(columns = {"latitude":"meridian"}, inplace = True)
# set country to be column index
df_latitude.set_index("country", inplace = True)
# save new dataframe to OUTPUT_FILENAME
df_latitude.to_csv(OUTPUT_FILENAME)
