import pandas as pd
import os 

EU_COUNTRIES_FILE = 'eu_countries.csv'
GDPPC_FILE = 'GDPPC-2010-constant.csv'
GDPPC_OUTPUT_FILE = 'GDPPC-2010-constant-reduced.csv'
LATITUDE_FILE = 'latitude-countries.csv'
LATITUDE_OUTPUT_FILE = 'latitude-countries-reduced.csv'
CAPACITY_FILE = 'all_energy_capacity.csv'
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
    dataframe_reduced = pd.merge(dataframe_to_reduce, nations,
                      how=JOIN_TYPE, on=JOIN_COLUMN)
    # write the result on file
    dataframe_reduced.to_csv(path_or_buf=output_file, index=False)

def replace_file(file_a, file_b):
    """substitute contents of file_a with file_b keeping the name of file_b
    @param file_a: path of the file which contents are to keep
    @param file_b: path of the file which name is to keep
    """
    os.remove(file_a)
    os.rename(file_b,file_a)

if __name__ == "__main__":
    # Reduce GDPPC dataset
    gdppc_dataframe = pd.read_csv(GDPPC_FILE)
    gdppc_dataframe.rename(columns={'Country':'country'},inplace=True)
    reduce_to_eu(gdppc_dataframe, GDPPC_OUTPUT_FILE)
    replace_file(GDPPC_FILE,GDPPC_OUTPUT_FILE)
    # Reduce LATITUDE dataset
    latitude_dataframe = pd.read_csv(LATITUDE_FILE)
    latitude_dataframe.rename(columns={'name':'country'},inplace=True)
    reduce_to_eu(latitude_dataframe, LATITUDE_OUTPUT_FILE)
    replace_file(LATITUDE_FILE,LATITUDE_OUTPUT_FILE)
    # Reduce CAPACITY dataset
    capacity_dataframe = pd.read_csv(CAPACITY_FILE)
    capacity_dataframe.rename(columns={'Country':'country'},inplace=True)
    reduce_to_eu(capacity_dataframe, CAPACITY_OUTPUT_FILE)
    replace_file(CAPACITY_FILE, CAPACITY_OUTPUT_FILE)
