""" The aim of this script is to extract 
    European Union members common to all datasets. 
    This way the results of the analysis from 
    each dataset can be compared without biases.
"""
import country_converter
import pandas as pd
import csv
import functools
import itertools as it
import os
# import full paths to files
import renewable_energy_analysis as rea

# csv filename for countries common to all datasets
COMMON_COUNTRIES = "renewable_energy_analysis/datasets/cleaned/common_countries.csv"

# get all files' full paths
GDP = rea.OriginalPaths.GDP
POLITICS = rea.OriginalPaths.POLITICS
CONSUMPTION = rea.OriginalPaths.CONSUMPTION
CAPACITY = rea.OriginalPaths.CAPACITY
WIND = rea.OriginalPaths.WIND

# remove last rows from CONSUMPTION as interfering;
TEMP_CONSUMPTION = "temp_consumption.csv"
# f for file in read mode
with open(CONSUMPTION, 'r') as r, open(TEMP_CONSUMPTION, 'w') as w:
    lines = r.readlines()
    lines = lines[:-12]
    writer = csv.writer(w, delimiter=',')
    w.write("{}\n".format(','.join(lines)))

# list of triples: (file, country_index, year_index)
FILES = [(GDP, ("column", 1)), 
         (POLITICS, ("column", 1)),
         (TEMP_CONSUMPTION, ("column", 0)), 
         (CAPACITY, ("column", 0)), 
         (WIND, ("header"))
         ]

# list of the European Union countries
eu28_countries = country_converter.CountryConverter().EU28["name_short"]


def extract_common_countries(FILES, eu28_countries):
    # store countries from data sets as type = set into a list
    eu_common_countries = [set(eu28_countries)]
    # retrieve countries for each dataset
    for i in range(len(FILES)):
        triple = FILES[i]
        # import file into pd dataframe
        df_countries = pd.read_csv(triple[0])
        # check where the countries lie in the dataframe
        if triple[1][0] == "column":
            # get the column index
            column_index = triple[1][1]
            # get the countries with no repetitions
            countries = df_countries.iloc[:, column_index].unique()
        if triple[1][0] == "row":
            # get the row index
            row_index = triple[1][1]
            # get the countries with no repetitions
            countries = df_countries.iloc[row_index, :].unique()
        if triple[1] == "header":
            # get the countries with no repetitions
            countries = df_countries.columns.values
        # map the code of countries to their names - consistency
        countries = country_converter.convert(
            names=list(countries), to='name_short', not_found=None)
        # UK and EL (Greece) do not get converted unfortunately)
        if "UK" in countries:
            countries.append("United Kingdom")
        if "EL" in countries:
            countries.append("Greece")
        # append countries for this data set to eu_common_countries as set
        eu_common_countries.append(set(countries))
    # actually extract common countries by sequential intersection
    eu_common_countries = functools.reduce(
        lambda A, B: A.intersection(B), eu_common_countries)
    # return countries common to all data sets
    return sorted(eu_common_countries)

# call function to get common countries
common_countries = extract_common_countries(FILES, eu28_countries)
with open(COMMON_COUNTRIES, 'w') as c:
    # writw to file with w
    w = csv.writer(c, delimiter=',')
    # header name
    w.writerow(["country"])
    # countries
    for country in common_countries:
        w.writerow([country])

os.remove(TEMP_CONSUMPTION)
# extract countries
#countries = df.iloc[:, 1]
#years = list(df.iloc[1, :])
# filter only for years
#years = list(filter(lambda i: i.isdigit(), years))
# type: from string to integer
#years = set(map(int, years))
# remove temp_file consumtion


