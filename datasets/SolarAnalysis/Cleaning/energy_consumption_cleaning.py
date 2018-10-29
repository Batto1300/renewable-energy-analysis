import pandas as pd 

# years and countries common to all datasets
COUNTRIES_YEARS = "SolarAnalysis/Cleaning/original/common_countries_and_years.csv"

# energy consumption csv file
ENERGY_CONSUMPTION = "SolarAnalysis/Cleaning/original/energy_consumption.csv"

# output 
OUTPUT_FILENAME = "SolarAnalysis/Cleaning/cleaned_energy_consumption.csv"


# importing countries and years common to all dataframes
df_COUNTRIES = pd.read_csv(COUNTRIES_YEARS, usecols=["country"])
df_years = pd.read_csv(COUNTRIES_YEARS, usecols=["year"])
# years as list
YEARS = list(df_years["year"])
# convert integers to strings
YEARS = list(map(str, YEARS))


# importing and cleaning energy consumption
df_energy_consumption = pd.read_csv(ENERGY_CONSUMPTION)
# the appropriate header row with the years is in row index 1
header = df_energy_consumption.iloc[1]
# change the first entry of header (= Million...) to "country"
header[0] = "country"
# set the new header
df_energy_consumption.columns = header
# drop last 3 columns 
df_energy_consumption.drop(columns = header[-3:], inplace = True)
# drop first 2 rows 
df_energy_consumption = df_energy_consumption[3:]
# merge on common countries with other dataframe 
df_energy_consumption = pd.merge(df_energy_consumption, df_COUNTRIES, on="country", how="inner")
# set index to country column 
df_energy_consumption.set_index("country", inplace = True)
# filter only for the years commom to all dataframes
df_energy_consumption = df_energy_consumption[YEARS]

# save to output filename
df_energy_consumption.to_csv(OUTPUT_FILENAME)