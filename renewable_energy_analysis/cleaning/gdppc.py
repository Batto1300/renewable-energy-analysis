import pandas as pd
import file_names as fn

# take absolute non os-dependant paths from file_names
GDPPC_PATH = fn.OriginalPaths.GDPPC
C_GDPPC_PATH = fn.CleanedPaths.GDPPC
YEARS_PATH = fn.CleanedPaths.YEARS
COUNTRIES_PATH = fn.CleanedPaths.COUNTRIES
# define hardcoded strings
COUNTRY_COLUMN_NAME = 'Country'
YEARS_COULMN_NAME = 'years'


# open files as dataframes
gdppc_df = pd.read_csv(open(GDPPC_PATH), skiprows=2)
# read years skipping the first row
years_list = open(YEARS_PATH).readlines()[1:]
# remove the newline character for every value in the list
years_list = list(map(lambda x: x[:-1],years_list))
countries_df = pd.read_csv(open(COUNTRIES_PATH))
# rename countries column
gdppc_df = gdppc_df.rename(columns={COUNTRY_COLUMN_NAME:COUNTRY_COLUMN_NAME.lower()})
# join used as a filter operation with countries and years dataframes
gdppc_df = pd.merge(gdppc_df,countries_df, on=COUNTRY_COLUMN_NAME.lower())
# filter out years setting the index so to filter only the columns
gdppc_df = gdppc_df.set_index(COUNTRY_COLUMN_NAME.lower())
gdppc_df = gdppc_df[years_list]
# save the resulting dataframe
gdppc_df.to_csv(C_GDPPC_PATH)
