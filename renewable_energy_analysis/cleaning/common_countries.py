""" This script extracts the European Union 
    members common to all datasets. 
    The csv file CONSUMPTION contains some non 
    important (explanatory text) end rows 
    which would create problems. Hence we create 
    a temporary file TEMP_CONSUMPTION that 
    has these rows removed.
"""
import country_converter
import pandas as pd
import csv
import functools
import os
# import class with full paths to files
import file_names as fn


# name of csv file to store countries common to all datasets
COMMON_COUNTRIES = fn.CleanedPaths.COUNTRIES
# get all original files' full paths
GDP = fn.OriginalPaths.GDP
POLITICS = fn.OriginalPaths.POLITICS
CONSUMPTION = fn.OriginalPaths.CONSUMPTION
CAPACITY = fn.OriginalPaths.CAPACITY
WIND = fn.OriginalPaths.WIND


def extract_common_countries(FILES, eu28_countries):
    """This function extract countries common to all 
        data sets. 
        Arguments of fucntion are FILES -> list of triples
        where elements are data set filename, column/row/header
        depending where the countries' names reside in the 
        data set and an integer for the respective row/column 
        position of the countries' names;
        eu28_countries: list of the European Union
        members countries.
    """
    # store countries from each data set into a list as type = set
    eu_common_countries = [set(eu28_countries)]
    # repeat the extraction for each data set
    for i in range(len(FILES)):
        triple = FILES[i]
        # import file into pd dataframe
        df_countries = pd.read_csv(triple[0])
        # check where the countries' names lie in the csv data
        if triple[1][0] == "column":
            # get the column index
            column_index = triple[1][1]
            # get the countries with no repetitions
            countries = df_countries.iloc[:, column_index].unique()
        # countries lie in one of the rows
        if triple[1][0] == "row":
            # get the row index
            row_index = triple[1][1]
            # get the countries' names with no repetitions
            countries = df_countries.iloc[row_index, :].unique()
        # countries lie in the header
        if triple[1] == "header":
            # get the countries' names
            countries = df_countries.columns.values
        # map the code (IT) of countries to their names (Italy)- consistency
        countries = country_converter.convert(
            names=list(countries), to='name_short', not_found=None)
        # UK and EL (Greece) do not get converted unfortunately
        if "UK" in countries:
            # replace would be better
            countries.append("United Kingdom")
        if "EL" in countries:
            # replace EL with Greece
            countries.append("Greece")
        # append countries for this data set to eu_common_countries as set
        eu_common_countries.append(set(countries))
    # extract countries common to all data sets by sequential intersection
    eu_common_countries = functools.reduce(
        lambda A, B: A.intersection(B), eu_common_countries)
    # return countries common to all data sets in alphabetical order
    return sorted(eu_common_countries)


# remove last rows from CONSUMPTION as interfering and create a temporary file
TEMP_CONSUMPTION = "temp_consumption.csv"
# open first file to read and second to write part of the first file
with open(CONSUMPTION, 'r') as r, open(TEMP_CONSUMPTION, 'w') as w:
    # read file CONSUMPTION and assign object to lines
    lines = r.readlines()
    # remove non important lines
    lines = lines[:-12]
    # write the modifies file to a temp file
    writer = csv.writer(w, delimiter=',')
    w.write("{}\n".format(','.join(lines)))
# list of triples: (file, countries' names location , country_index)
FILES = [(GDP, ("column", 1)),
         (POLITICS, ("column", 1)),
         (TEMP_CONSUMPTION, ("column", 0)),
         (CAPACITY, ("column", 0)),
         (WIND, ("header"))
         ]
# list of the European Union countries
eu28_countries = country_converter.CountryConverter().EU28["name_short"]
# call function to get common countries to all data sets
common_countries = extract_common_countries(FILES, eu28_countries)
# store these common countries in a csv file
with open(COMMON_COUNTRIES, 'w') as c:
    # write to file comma separator
    w = csv.writer(c, delimiter=',')
    # header name
    w.writerow(["country"])
    # write countries' names each on a new line
    for country in common_countries:
        w.writerow([country])
# remove the temporarily created file
os.remove(TEMP_CONSUMPTION)
