import file_names as fn
import pandas as pd
import csv

#Options for Pandas
pd.set_option('display.width', 200000)
pd.set_option('max.columns', 200)
#File Paths
WIND = fn.OriginalPaths.WIND
CLEANED_WIND = fn.CleanedPaths.WIND
YEARS = fn.CleanedPaths.YEARS
COUNTRIES = fn.CleanedPaths.COUNTRIES

#Importing Files
df_wind = pd.read_csv(open(WIND))
#Removing Redundant Columns
to_drop = ['Time','step','Date','Month','Day','Hour']
df_wind.drop(to_drop, inplace=True, axis=1)
#Renaming Columns
df_wind.rename(columns={'PL':'Poland','ES':'Spain','UK':'United Kingdom','CZ':'Czech Republic','BG':'Bulgaria','NO':'Norway',
                   'RO':'Romania','DK':'Denmark','HU':'Hungary','EE':'Estonia','CH':'Switzerland', 'IE':'Ireland',
                   'SE':'Sweden','PT':'Portugal','AT':'Austria','BE':'Belgium','EL':'Greece','FI':'Finland','LT':'Lithuania',
                   'LU':'Luxembourg','LV':'Latvia','SK':'Slovakia','NL':'Netherlands','IT':'Italy','DE':'Germany',
                   'FR':'France','SI':'Slovenia','HR':'Croatia'},inplace=True)
#Filter by Common Years
years_df = open(YEARS).readlines()[1:]
df_wind = df_wind[df_wind['Year'].isin(years_df)]
#Calculating Mean Per Year For Each Country
def MeanWind(x):
    return df_wind.groupby('Year').sum()
x = df_wind.columns
MeanWind(x)
df_wind = MeanWind(x)
#Transpose DataFrame to appropriate format
df_wind_t = pd.DataFrame.transpose(df_wind)
#Filter DataFrame by Common Countries
df_countries = pd.read_csv(open(COUNTRIES), index_col=0)
df_wind_t = pd.DataFrame.join(df_wind_t, df_countries, how='inner')
#Saving cleaned data as new csv file
df_wind_t.to_csv(CLEANED_WIND, index_label='country')
print(df_wind_t)

