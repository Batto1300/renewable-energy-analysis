import pandas as pd
import os

EU_COUNTRIES_FILE = 'original/eu_countries.csv'
GDPPC_FILE = 'original/GDPPC-2010-constant.csv'
GDPPC_OUTPUT_FILE = 'adjusted/GDPPC-2010-constant-reduced.csv'
LATITUDE_FILE = 'original/latitude-countries.csv'
LATITUDE_OUTPUT_FILE = 'adjusted/latitude-countries-reduced.csv'
CAPACITY_FILE = 'original/all-energy-capacity.csv'
CAPACITY_OUTPUT_FILE = 'adjusted/all-energy-capacity-reduced-eu.csv'
POLITICAL_ORIENTATION_FILE = 'original/CPDS-1960-2016-Update-2018.csv'
GDP_FILE = 'original/GDP-2010-constant.csv'
GDP_OUTPUT_FILE = 'adjusted/GDP-2010-constant.csv'
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
    dataframe_reduced = pd.merge(dataframe_to_reduce, nations,
                                 how=JOIN_TYPE, on=JOIN_COLUMN)
    # write the result on file
    dataframe_reduced.to_csv(path_or_buf=output_file, index=False)

if __name__ == "__main__":
    # Reduce GDPPC dataset
    gdppc_dataframe = pd.read_csv(GDPPC_FILE)
    gdppc_dataframe.rename(columns={'Country': 'country'}, inplace=True)
    reduce_to_eu(gdppc_dataframe, GDPPC_OUTPUT_FILE)
    # Reduce LATITUDE dataset
    latitude_dataframe = pd.read_csv(LATITUDE_FILE)
    latitude_dataframe.rename(columns={'name': 'country'}, inplace=True)
    reduce_to_eu(latitude_dataframe, LATITUDE_OUTPUT_FILE)
    # Reduce CAPACITY dataset
    capacity_dataframe = pd.read_csv(CAPACITY_FILE)
    capacity_dataframe.rename(columns={'Country':'country'},inplace=True)
    reduce_to_eu(capacity_dataframe, CAPACITY_OUTPUT_FILE)
    # Reduce Political Orientation dataset
    orientation_dataframe = pd.read_csv(POLITICAL_ORIENTATION_FILE)
    reduce_to_eu(orientation_dataframe, 'tmp.csv')
    # Reduce GDP dataset
    gdp_dataframe = pd.read_csv(GDP_FILE, skiprows=2)
    gdp_dataframe.rename(columns={'Country': 'country'}, inplace=True)
    gdp_dataframe = gdp_dataframe[gdp_dataframe['IndicatorName'].str.contains(
        'Final consumption expenditure')]
    gdp_dataframe.drop(['IndicatorName'], axis=1, inplace=True)
    reduce_to_eu(gdp_dataframe, GDP_OUTPUT_FILE)
