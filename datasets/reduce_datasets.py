import pandas as pd


EU_COUNTRIES_FILE = 'eu_countries.csv'
GDPPC_FILE = 'GDPPC-2010-constant.csv'
GDPPC_OUTPUT_FILE = 'GDPPC-2010-constant-reduced.csv'
LATITUDE_FILE = 'latitude-countries.csv'
LATITUDE_OUTPUT_FILE = 'latitude-countries-reduced.csv'
CAPACITY_FILE = 'all-energy-capacity-eu-adj.csv'
CAPACITY_OUTPUT_FILE = 'all-energy-capacity-reduced-eu.csv'
JOIN_COLUMN = 'country'
JOIN_TYPE = 'inner'

def reduce_to_eu(dataframe_to_reduce, output_file):
    """
    perform a JOIN_TYPE join between datasets_to_reduce
    and a Series of countries on JOIN_COLUMN.
    @param dataframe_to_reduce: pandas dataframe with a 'country' column
    """
    nations = pd.read_csv(EU_COUNTRIES_FILE)
    # assert that the original dataset has all the countries
    countries_diff = set(nations.country.unique()) - \
        set(dataframe_to_reduce.country.unique())
    assert not countries_diff, countries_diff
    # perform the join
    gdp_eu = pd.merge(dataframe_to_reduce, nations,
                      how=JOIN_TYPE, on=JOIN_COLUMN)
    # write the result on file
    gdp_eu.to_csv(path_or_buf=output_file)

# Reduce GDPPC dataset
gdppc_dataframe = pd.read_csv(GDPPC_FILE, skiprows=2)
reduce_to_eu(gdppc_dataframe, GDPPC_OUTPUT_FILE)
# Reduce LATITUDE dataset
latitude_dataframe = pd.read_csv(LATITUDE_FILE)
latitude_dataframe.rename(
    columns={'country': 'country_code', 'name': 'country'}, inplace=True)
reduce_to_eu(latitude_dataframe, LATITUDE_OUTPUT_FILE)
# Reduce CAPACITY dataset
capacity_dataframe = pd.read_csv(CAPACITY_FILE)
"""column renamed manually because the following doesn't seem to work,it may be a bug:
            capacity_dataframe.rename(columns={'Country/area':'country'})
"""
reduce_to_eu(capacity_dataframe, CAPACITY_OUTPUT_FILE)

