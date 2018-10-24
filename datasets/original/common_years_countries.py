import country_converter 
import pandas as pd
import csv 
import functools

# list of european countries belonging to ...
european_countries = country_converter.CountryConverter().EU28

#list to append sets of countries from dataframes
european_countries = [set(european_countries["name_short"])]


""" For ENERGY CAPACITY"""
ENERGY_CAPACITY = "all_energy_capacity.csv"
df_energy_capacity = pd.read_csv(ENERGY_CAPACITY, usecols=["Country"])
european_countries.append(set(df_energy_capacity["Country"]))


""" For WIND_PRODUCTION """
WIND_PRODUCTION = "wind_production.csv"

header = []
with open(WIND_PRODUCTION, 'r') as csv_file:
    # set for reading mode
    csv_reader = csv.reader(csv_file)
    # get only first line - the header row
    header = next(csv_reader) # this is the name of the file
    # append row (now a list of column indexes) as a set to headers
    header.append(header)

header = country_converter.convert(names=header, to='name_short', not_found=None)
header.append('United Kingdom')
header=set(header)
# appending countries
european_countries.append(header)


""" For ENERGY CONSUMPTION """
ENERGY_CONSUMPTION = "energy_consumption.csv"

df_energy_consumption = pd.read_csv(ENERGY_CONSUMPTION)
# inspect
print(df_energy_consumption.head())
# countries are in the first column - append it to list
european_countries.append(set(df_energy_consumption.iloc[:,0]))


""" For GDP """ 
GDP = "GDP_2010_constant.csv" 
df_gdp = pd.read_csv(GDP)
# inspect 
print(df_gdp.head())
# countrie are in the second column
european_countries.append(set(df_gdp.iloc[:,1]))


""" For Politics """
POLITICS = "CPDS_1960_2016_Update-2018.csv" 
df_politics = pd.read_csv(POLITICS, usecols=["country"])
# append as a set to list
european_countries.append(set(df_politics["country"]))
# sequential intersection on the list of sets    
common_countries = functools.reduce(lambda A, B: A.intersection(B), european_countries) 
# common years =

print(common_countries)