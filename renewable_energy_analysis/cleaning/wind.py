import file_names as fn
import country_converter as cc
import pandas as pd

#Options for Pandas
pd.set_option('display.width', 5000)
pd.set_option('max.columns', 5000)

#File Paths
Wind = fn.OriginalPaths.WIND
Cleaned_Wind = fn.CleanedPaths.WIND
Years = fn.CleanedPaths.YEARS
Countries = fn.CleanedPaths.COUNTRIES
#Hardcoded Strings
Country_Column_Name = 'country'
Years_Column_Name = 'years'

#Wind Production List
df_wind = pd.read_csv(open(Wind))
#Importing Common Years List
years_list = open(Years).readlines()[1:]
years_list = list(map(lambda x: x[:-1],years_list))
df_wind = df_wind[df_wind['Year'].isin(years_list)]
#Importing Common Countries List
df_countries = pd.read_csv(open(Countries))
#Renaming Country Labels
df_wind.rename(columns={'PL':'Poland','ES':'Spain','UK':'United Kingdom','CZ':'Czech Republic','BG':'Bulgaria','NO':'Norway',
                   'RO':'Romania','DK':'Denmark','HU':'Hungary','EE':'Estonia','CH':'Switzerland', 'IE':'Ireland',
                   'SE':'Sweden','PT':'Portugal','AT':'Austria','BE':'Belgium','EL':'Greece','FI':'Finland','LT':'Lithuania',
                   'LU':'Luxembourg','LV':'Latvia','SK':'Slovakia','NL':'Netherlands','IT':'Italy','DE':'Germany',
                   'FR':'France','SI':'Slovenia','HR':'Croatia'},inplace=True)

print(df_wind)