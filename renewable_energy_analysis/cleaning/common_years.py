""" This script extracts the years
    common to all datasets. 
    The csv file CONSUMPTION contains some non 
    important (explanatory text) end rows 
    which would create problems. Hence we create 
    a temporary file TEMP_CONSUMPTION with
    these rows removed.
"""
import pandas as pd
import csv
import functools
import itertools as it
import os
# import class with full paths to files
import file_names as fn


# path of csv file to store years common to all datasets
COMMON_YEARS = fn.CleanedPaths.YEARS
# get paths of individual original files
GDP = fn.OriginalPaths.GDP
POLITICS = fn.OriginalPaths.POLITICS
CONSUMPTION = fn.OriginalPaths.CONSUMPTION
CAPACITY = fn.OriginalPaths.CAPACITY
WIND = fn.OriginalPaths.WIND


def extract_common_years(FILES):
    """This function extract the years common to all 
        data sets. 
        Arguments of fucntion are FILES -> list of triples
        where elements are data set filename, column/row/header
        depending where the years reside in the 
        data set and an integer for the respective row/column 
        position of the year values;
    """
    # store years from each data set in a list 
    common_years = []
    # repeat the extraction of year values for each data set
    for i in range(len(FILES)):
        triple = FILES[i]
        # import file into pd dataframe
        df_mixed_years = pd.read_csv(triple[0])
        # check where the years lie in the dataframe
        if triple[1][0] == "column":
            # get the column index
            column_index = triple[1][1]
            # get the year values with no repetitions
            mixed_years = df_mixed_years.iloc[:, column_index]
        # years lie in one of the rows
        elif triple[1][0] == "row":
            # get the row index
            row_index = triple[1][1]
            # get the years with no repetitions
            mixed_years = df_mixed_years.iloc[row_index, :]
        # countries lie in the header
        else:
            # get the year values with no repetitions
            mixed_years = df_mixed_years.columns.values
        # mixed_years: pandas object to list type
        mixed_years = list(mixed_years)
        # filter only the years - some elements of the list may be strings
        years = []
        # loop over each element in the list
        for element in mixed_years:
            # try to convert the element to an integer - string would fail
            try:
                year = int(element)
                # if the conversion is successfull that element will be a year
                years.append(year)
            # if the element is a string the int function would raise a ValueError
            except ValueError:
                # ignore this element/string
                pass
        # now append the list of years, type = int
        common_years.append(set(years))
    # actually extract common years by sequential intersection
    common_years = functools.reduce(
        lambda A, B: A.intersection(B), common_years)
    # return years common to all data sets in ascending order
    return sorted(common_years)


# remove last rows from CONSUMPTION as interfering;
TEMP_CONSUMPTION = "temp_consumption.csv"
# f for file in read mode
with open(CONSUMPTION, 'r') as r, open(TEMP_CONSUMPTION, 'w') as w:
    # read file CONSUMPTION and assign object to lines
    lines = r.readlines()
    # remove non important lines
    lines = lines[:-12]
    # write the modifies file to a temp file
    writer = csv.writer(w, delimiter=',')
    w.write("{}\n".format(','.join(lines)))
# list of triples: (file, years' location , years_index position)
FILES = [(GDP, ("row", 1)),
         (POLITICS, ("column", 0)),
         (TEMP_CONSUMPTION, ("row", 1)),
         (CAPACITY, ("header")),
         (WIND, ("column", 3))
         ]
# call function to extract common years from all datasets
common_years = extract_common_years(FILES)
# store the common years to a csv file ready for analysis
with open(COMMON_YEARS, 'w') as y:
    # write to file with w
    w = csv.writer(y, delimiter=',')
    # header name
    w.writerow(["years"])
    # years
    for year in common_years:
        w.writerow([year])
# remove temporary file
os.remove(TEMP_CONSUMPTION)
