import pandas as pd
import os
import csv

# original raw file
FILENAME = "SolarAnalysis/Cleaning/original/all_energy_capacity.csv"

# years and countries common to all datasets
COUNTRIES_YEARS = "SolarAnalysis/Cleaning/original/common_countries_and_years.csv"

# output file for cleaned dataset
OUTPUT_FILENAME = "SolarAnalysis/Cleaning/cleaned_all_energy_capacity.csv"

# filling missing country in the columns
with open(FILENAME, 'r') as o, open(OUTPUT_FILENAME, "w") as w:  
    nation_reader = csv.reader(o)
    header = next(nation_reader)
    header[0] = "country"
    w.write("{}\n".format(','.join(header)))
    row = next(nation_reader)
    while row:
        for i in range(3):
            if i == 0:
                country = row[0]
            else:
                row[0] = country
            w.write("{}\n".format(','.join(row)))
            try:
                row = next(nation_reader)
            except StopIteration:
                row = None   # empty address


# reads and converts the csv file into a datafreame 
df_countries = pd.read_csv(COUNTRIES_YEARS, usecols=["country"])
df_years = pd.read_csv(COUNTRIES_YEARS, usecols=["year"])
years = list(df_years["year"])
years = list(map(str, years))
# importing energy capacity
columns_to_skip = ['Indicator']
df_energy_capacity = pd.read_csv(OUTPUT_FILENAME, usecols=lambda x: x not in columns_to_skip)
df_energy_capacity = pd.merge(df_energy_capacity, df_countries, on = "country", how="inner")
df_energy_capacity = df_energy_capacity[df_energy_capacity["Technology"] == "Solar"]
df_energy_capacity.set_index(["country", "Technology"], inplace = True)
df_energy_capacity = df_energy_capacity[years]

# Remove all countries which contain all missing vales in all energy resources
#for i in df.index.levels[0]:   # list of countries, type = string
#   if pd.isnull(df.loc[i, "2000" : "2017"]).all().all():
 #       df.drop(i, inplace = True)

##.reset_index(level = None, inplace = True



df_energy_capacity.to_csv(OUTPUT_FILENAME)