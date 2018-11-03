""" This script cleans the original data set 
    containing the cumulative energy capacity figures 
    for all European countries.
    Firsly, we replace the missing values along the 
    first column with the name of the country. 
    Secondly, we filter the dataset for those 
    countries and years which are common to 
    all datasets. 
"""


import pandas as pd
import os
import csv

# original data (csv file) - cumulative energy capacity figures
FILENAME = "SolarAnalysis/Cleaning/original/all_energy_capacity.csv"

# years and countries common to all datasets
COUNTRIES = "SolarAnalysis/Cleaning/original/common_countries.csv"
YEARS = "SolarAnalysis/Cleaning/original/common_years.csv"

# name of new csv file to store the new cleaned and filtered dataset
OUTPUT_FILENAME = "SolarAnalysis/Cleaning/cleaned_all_energy_capacity.csv"

# filling missing country in the first column of dataset
with open(FILENAME, 'r') as o, open(OUTPUT_FILENAME, "w") as w:
    # assign reader object to a variable - our "eyes"
    nation_reader = csv.reader(o)
    # get the header row - first line
    header = next(nation_reader)
    # change "Country" to "country" - common to all data sets
    header[0] = "country"
    # write the header to the output file opened in writing mode 'w'
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
            # write the row to the output file (w)
            w.write("{}\n".format(','.join(row)))
            try:
                # read the next line/row
                row = next(nation_reader)
            # if next line is empty, python throws an error (StopIteration)
            except StopIteration:
                # in this case set the row to None - this way "while row" will give False
                row = None


# Read the cleaned file/data set into a dataframe but skip useless column
columns_to_skip = ['Indicator']
# read the file withou the above column
df_energy_capacity = pd.read_csv(
    OUTPUT_FILENAME, usecols=lambda x: x not in columns_to_skip)

# import countries which are common to all data sets of the report
df_countries = pd.read_csv(COUNTRIES)

# filter the energy capacity data set by the common countries using merge
df_energy_capacity = pd.merge(
    df_energy_capacity, df_countries, on="country", how="inner")
# filter for solar energy (the focus of my research) = excluding hydro, wind 
df_energy_capacity = df_energy_capacity[df_energy_capacity["Technology"] == "Solar"]
# set the first two columns as index columns so that we can filter for the common years
df_energy_capacity.set_index(["country", "Technology"], inplace=True)

# import years which are common to all data sets of the report
df_years = pd.read_csv(YEARS)
# from dataframe object to list
years = list(df_years["year"])
# convert years from integer to string type
years = list(map(str, years))

# filter the dataframe for only those years common to all countries
df_energy_capacity = df_energy_capacity[years]

# write cleaned and transformed dataset to a new file ready for analysis
df_energy_capacity.to_csv(OUTPUT_FILENAME)
