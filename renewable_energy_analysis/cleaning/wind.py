import file_names as fn
import country_converter as cc
import numpy as np
import pandas as pd

#Options for Pandas
pd.set_option('display.width', 200000)
pd.set_option('max.columns', 200)

#File Paths
Wind = fn.OriginalPaths.WIND
Cleaned_Wind = fn.CleanedPaths.WIND
Years = fn.CleanedPaths.YEARS
Countries = fn.CleanedPaths.COUNTRIES


#Wind Production List
df_wind = pd.read_csv(open(Wind))
#Importing Common Years List
years_list = open(Years).readlines()[1:]
#Common years in wind data
years_list = list(map(lambda x: x[:-1],years_list))
df_wind = df_wind[df_wind['Year'].isin(years_list)]
#Indexing Based on Common Years
df_wind.set_index('Year', drop=True, inplace=True)
#Removing Redundant Data
to_drop = ['Time','step','Date','Month','Day','Hour']
df_wind.drop(to_drop, inplace=True, axis=1)
#Reshaping Data
df_wind.rename(columns={'PL':'Poland','ES':'Spain','UK':'United Kingdom','CZ':'Czech Republic','BG':'Bulgaria','NO':'Norway',
                   'RO':'Romania','DK':'Denmark','HU':'Hungary','EE':'Estonia','CH':'Switzerland', 'IE':'Ireland',
                   'SE':'Sweden','PT':'Portugal','AT':'Austria','BE':'Belgium','EL':'Greece','FI':'Finland','LT':'Lithuania',
                   'LU':'Luxembourg','LV':'Latvia','SK':'Slovakia','NL':'Netherlands','IT':'Italy','DE':'Germany',
                   'FR':'France','SI':'Slovenia','HR':'Croatia'},inplace=True)
df_wind = pd.DataFrame.transpose(df_wind)


#Countries
df_countries = pd.read_csv(open(Countries))


print(df_wind)