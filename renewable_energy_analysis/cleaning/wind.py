import file_names as fn
import country_converter as cc
import numpy as np
import pandas as pd
import csv

#Options for Pandas
pd.set_option('display.width', 200000)
pd.set_option('max.columns', 200)
#File Paths
Wind = fn.OriginalPaths.WIND
Cleaned_Wind = fn.CleanedPaths.WIND
Years = fn.CleanedPaths.YEARS
Countries = fn.CleanedPaths.COUNTRIES
#Hardcoded Strings
Country_Column_Name = 'country'
Years_Column_Name = 'years'

#Importing Files
df_wind = pd.read_csv(open(Wind))
years_df = open(Years).readlines()[1:]
countries_df = pd.read_csv(Countries)

#Data Formatting
to_drop = ['Time','step','Date','Month','Day','Hour']
df_wind.drop(to_drop, inplace=True, axis=1)
df_wind.rename(columns={'PL':'Poland','ES':'Spain','UK':'United Kingdom','CZ':'Czech Republic','BG':'Bulgaria','NO':'Norway',
                   'RO':'Romania','DK':'Denmark','HU':'Hungary','EE':'Estonia','CH':'Switzerland', 'IE':'Ireland',
                   'SE':'Sweden','PT':'Portugal','AT':'Austria','BE':'Belgium','EL':'Greece','FI':'Finland','LT':'Lithuania',
                   'LU':'Luxembourg','LV':'Latvia','SK':'Slovakia','NL':'Netherlands','IT':'Italy','DE':'Germany',
                   'FR':'France','SI':'Slovenia','HR':'Croatia'},inplace=True)

df_wind = df_wind.isin(countries_df)
df_wind = df_wind[df_wind['Year'].isin(years_df)]

print(df_wind.head(5))