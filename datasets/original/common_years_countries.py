import country_converter
import pandas as pd
import csv
import functools
import itertools as it



# list of the European Union countries
european_countries = country_converter.CountryConverter().EU28
# lists to store countries and years from each data set. Item Type = set
european_countries = [set(european_countries["name_short"])]
years = []


# For ENERGY CAPACITY
ENERGY_CAPACITY = "all_energy_capacity.csv"

# countries:
df_countries = pd.read_csv(ENERGY_CAPACITY, usecols=["Country"])
countries = set(df_countries["Country"])
# United Kingdom reported as UK - consistency
countries.add("United Kingdom")
european_countries.append(countries)

# years:
df_years = pd.read_csv(ENERGY_CAPACITY, nrows=0)
header_years = df_years.columns.values
# filter only for years. type = string
header_years = list(filter(lambda i: i.isdigit(), header_years))
# type = integer - does it matter?
header_years = list(map(int, header_years))
# append column_years to list as set type
years.append(set(header_years))


# For WIND_PRODUCTION
WIND_PRODUCTION = "wind_production.csv"

# countries:
df_countries = pd.read_csv(WIND_PRODUCTION, nrows=0)
# convert dataframe object to list
header_countries = list(df_countries.columns.values)
# countries appear as ISO2 code - convert to full name
header_countries = country_converter.convert(
    names=header_countries, to='name_short', not_found=None)
# uppercasing the first letter for each country name
#header_countries = [word[:1].upper() + word[1:] for word in header_countries]
# Issue: UK and EL (Greece) were not found:
header_countries.append('United Kingdom')
header_countries.append('Greece')
# append header_countries to list as set type
european_countries.append(set(header_countries))

# years:
df_years = pd.read_csv(WIND_PRODUCTION, usecols=["Year"])
# the column contains only years already as integers
years.append(set(df_years["Year"]))


# For ENERGY CONSUMPTION
ENERGY_CONSUMPTION = "energy_consumption.csv"

# countries:
df_countries = pd.read_csv(ENERGY_CONSUMPTION)
# countries are in the first column - append it to list
european_countries.append(set(df_countries.iloc[:, 0]))

# years:
df_years = pd.read_csv(ENERGY_CONSUMPTION, nrows=3) # note if nrows is 3 pandas does no recognise the headers and returns thems as floats
# years are in row index 1
df_years = list(df_years.iloc[1])
# filter only the years - some years are floats (.0)
header_years = []
for item in df_years:
    try:
        year = int(item)
        header_years.append(year)
    except ValueError:
        pass
# append to list
years.append(set(header_years))


# For GDP
GDP = "GDP_2010_constant.csv"

# countries:
df_countries = pd.read_csv(GDP)
# countrie are in the second column
european_countries.append(set(df_countries.iloc[:, 1]))

# years:
df_years = pd.read_csv(GDP, nrows=3)
# years are in row index 1
header_years = list(df_years.iloc[1])
# filter only for years. type = string
header_years = list(filter(lambda i: i.isdigit(), header_years))
# type = integer -  when doing the intersection we need all years in the sampe type
header_years = set(map(int, header_years)) #  can it be as set?
# append column_years to list as set type
years.append(header_years)


# For Politics
POLITICS = "CPDS_1960_2016_Update-2018.csv"

# countries & years
df_countries = pd.read_csv(POLITICS, usecols=["year","country"])
# append countries as a set to list
european_countries.append(set(df_countries["country"]))
# append years as a set to list
df_years = list(df_countries["year"])
header_years = []
for item in df_years:
    try:
        year = int(item)
        header_years.append(year)
    except ValueError:
        pass
years.append(set(header_years))


# sequential intersection on the list of sets for countries and years
common_countries = functools.reduce(
    lambda A, B: A.intersection(B), european_countries)

common_years = functools.reduce(
    lambda A, B: A.intersection(B), years)

common_countries = sorted(list(common_countries))

common_years = sorted(list(common_years))

# write to a csv file
with open("../common_countries.csv", 'w') as c, open("../common_years.csv", 'w') as y: 
    # writw to file with w
    w = csv.writer(c, delimiter = ',')
    # header names
    w.writerow(["country"])
    # countries and years
    for country in common_countries:
        w.writerow([country])
    w = csv.writer(y, delimiter = ',')
    # header names
    w.writerow(["year"])
    # countries and years
    for year in common_years:
        w.writerow([str(year)])
    

        