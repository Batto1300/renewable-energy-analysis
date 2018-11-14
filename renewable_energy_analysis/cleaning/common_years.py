""" The aim of this script is to extract 
    years common to all datasets. 
    This way the results of the analysis from 
    each dataset can be compared without biases.
"""
import pandas as pd
import csv
import functools
import itertools as it
import os
# import full paths to files
import renewable_energy_analysis as rea

# csv filename for years common to all datasets
COMMON_YEARS = "renewable_energy_analysis/datasets/cleaned/common_years.csv"

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

# list of tuples: (file, (where ,year_index))
FILES = [(GDP, ("row", 1)),
         (POLITICS, ("column", 0)),
         (TEMP_CONSUMPTION, ("row", 1)),
         (CAPACITY, ("header")),
         (WIND, ("column", 3))
         ]


def extract_common_years(FILES):
    # store years from data sets as type = set into a list
    common_years = []
    # retrieve years for each dataset
    for i in range(len(FILES)):
        twople = FILES[i]
        # import file into pd dataframe
        df_mixed_years = pd.read_csv(twople[0])
        # check where the years lie in the dataframe
        if twople[1][0] == "column":
            # get the column index
            column_index = twople[1][1]
            # get the years with no repetitions
            mixed_years = df_mixed_years.iloc[:, column_index]
        if twople[1][0] == "row":
            # get the row index
            row_index = twople[1][1]
            # get the years with no repetitions
            mixed_years = df_mixed_years.iloc[row_index, :]
        if twople[1] == "header":
            # get the years with no repetitions
            mixed_years = df_mixed_years.columns.values
        # years: pandas object to list 
        mixed_years = list(mixed_years)
        # filter only the years - some years are floats (.0)
        years = []
        for year in mixed_years:
            try:
                year = int(year)
                years.append(year)
            except ValueError:
                pass
        # convert to integers if strings - consistency
        #years = map(int, years)
        # append to list of years
        common_years.append(set(years))
    # actually extract common years by sequential intersection
    common_years = functools.reduce(
        lambda A, B: A.intersection(B), common_years)
    # return years common to all data sets
    return sorted(common_years)

# call function to get common years
common_years = extract_common_years(FILES)
# write years to a csv file ready for analysis
with open(COMMON_YEARS, 'w') as y:
    # writw to file with w
    w = csv.writer(y, delimiter=',')
    # header name
    w.writerow(["years"])
    # years
    for year in common_years:
        w.writerow([year])

# remove temporary file
os.remove(TEMP_CONSUMPTION)

