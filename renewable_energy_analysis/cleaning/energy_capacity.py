""" This script cleans the original data set 
    containing the cumulative energy capacity figures 
    for all European countries.
    Firsly, we replace the missing values along the 
    first column with the name of the country so that 
    manipulation of dataset becomes easier. 
    Secondly, we filter the dataset for those 
    countries and years which are common to 
    all datasets. 
"""
import pandas as pd
import os
import csv
# import class with full paths to files
import file_names as fn


# original data (csv file) - cumulative energy capacity figures
ORIGINAL_ENERGY_CAPACITY = fn.OriginalPaths.CAPACITY
# countries common to all datasets
COUNTRIES = fn.CleanedPaths.COUNTRIES
# years common to all datasets
YEARS = fn.CleanedPaths.YEARS
# name of new csv file to store the new cleaned and filtered dataset
CLEANED_ENERGY_CAPACITY = fn.CleanedPaths.CAPACITY


# filling missing country in the first column of dataset
with open(ORIGINAL_ENERGY_CAPACITY, 'r') as o, open(CLEANED_ENERGY_CAPACITY, "w") as w:
    # assign reader object to a variable - our "eyes"
    nation_reader = csv.reader(o)
    # get the header row - first line
    header = next(nation_reader)
    # change "Country" to "country" - common to all data sets
    header[0] = "country"
    # write the header to the CLEANED file opened in writing mode 'w'
    w.write("{}\n".format(','.join(header)))
    # now skip to second line - the data
    row = next(nation_reader)
    # fill the two empty cells below each country with the name of that country
    while row:  # as long as the row is not empty
        # each country name must occur 3 times
        for i in range(3):
            # every 3*k row, the 1st cell contains the name of the country...
            if i == 0:
                # get the name of the country
                country = row[0]
            # ... while the 2 cells below are empty
            else:
                # fill those empty cells with the right country name
                row[0] = country
            # write the row to the CLEANED file (w)
            w.write("{}\n".format(','.join(row)))
            try:
                # read the next line/row
                row = next(nation_reader)
            # if next line is empty, python throws an error (StopIteration)
            except StopIteration:
                # in this case set the row to None - this way "while row" will give False
                row = None
# import countries which are common to all data sets 
df_countries = pd.read_csv(COUNTRIES)
# Read the data set with the filled columns into a dataframe but skip useless column
columns_to_skip = ['Indicator']
# read the file without the above column
df_energy_capacity = pd.read_csv(
    CLEANED_ENERGY_CAPACITY, usecols=lambda x: x not in columns_to_skip)
# change UK to United Kingdom
df_energy_capacity.loc[df_energy_capacity["country"] == "UK", "country"] = "United Kingdom"
# filter the energy capacity data set by the common countries using merge
df_energy_capacity = pd.merge(
    df_energy_capacity, df_countries, on="country", how="inner") 
# set the first two columns as index columns so that we can filter for the common years
df_energy_capacity.set_index(["country", "Technology"], inplace=True)
# import years which are common to all data sets of the report
df_years = pd.read_csv(YEARS)
# from pandas object to list
years = list(df_years["years"])
# convert years from integer to string type
years = list(map(str, years))
# filter the dataframe for only those years common to all countries
df_energy_capacity = df_energy_capacity[years]
# write cleaned and transformed dataset to a new file ready for analysis
df_energy_capacity.to_csv(CLEANED_ENERGY_CAPACITY)
