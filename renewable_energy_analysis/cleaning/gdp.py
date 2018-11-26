import pandas as pd
import file_names as fn

# take absolute non os-dependant paths from file_names
GDP_PATH = fn.OriginalPaths.GDP
C_GDP_PATH = fn.CleanedPaths.GDP
YEARS_PATH = fn.CleanedPaths.YEARS
COUNTRIES_PATH = fn.CleanedPaths.COUNTRIES
# define hardcoded strings
IND_COL_NAME = 'IndicatorName'
GDP_IND_VALUE = 'Gross Domestic Product (GDP)'
COUNTRY_COLUMN_NAME = 'Country'
YEARS_COULMN_NAME = 'years'


# open files as dataframes
gdp_df = pd.read_csv(open(GDP_PATH), skiprows=2)
# read years skipping the first row
years_list = open(YEARS_PATH).readlines()[1:]
# remove the newline character for every value in the list
years_list = list(map(lambda x: x[:-1],years_list))
countries_df = pd.read_csv(open(COUNTRIES_PATH))
# select values referring to GDP only
gdp_df = gdp_df[gdp_df[IND_COL_NAME] == GDP_IND_VALUE]
# rename countries
gdp_df = gdp_df.rename(columns={COUNTRY_COLUMN_NAME:COUNTRY_COLUMN_NAME.lower()})
# drop indicator column (every row has the same value now)
gdp_df = gdp_df.drop([IND_COL_NAME], axis=1)
# join used as a filter operation with countries and years dataframes
gdp_df = pd.merge(gdp_df,countries_df, on=COUNTRY_COLUMN_NAME.lower())
# filter out years setting the index so to filter only the columns
gdp_df = gdp_df.set_index(COUNTRY_COLUMN_NAME.lower())
gdp_df = gdp_df[years_list]
gdp_df = gdp_df.applymap(lambda x: x.replace(".",""))
# save the resulting dataframe
gdp_df.to_csv(C_GDP_PATH)
