import file_names as fn
import country_converter as cc
import pandas as pd

#Options for Pandas
pd.set_option('display.width', 5000)
pd.set_option('max.columns', 5000)

#File Paths
WIND_PATH = fn.OriginalPaths.WIND
C_WIND_PATH = fn.CleanedPaths.WIND
YEARS_PATH = fn.CleanedPaths.YEARS
COMMON_COUNTRIES = fn.CleanedPaths.COUNTRIES

#Wind Production List
wp = pd.read_csv(open(WIND_PATH))

#Wind Production Filter by Common Years
years_list = open(YEARS_PATH).readlines()[1:]
years_list = list(map(lambda x: int(x[:-1]),years_list))
wp = wp[wp['Year'].isin(years_list)]
#Creating Common Countires List
countries_list = open(COMMON_COUNTRIES).readlines()[1:]
countries_list = list(map(lambda x: x.strip(), countries_list))

#DataFrame Formatting
    #Changing Country Names
wp.rename(columns={'PL':'Poland','ES':'Spain','UK':'United Kingdom','CZ':'Czech Republic','BG':'Bulgaria','NO':'Norway',
                   'RO':'Romania','DK':'Denmark','HU':'Hungary','EE':'Estonia','CH':'Switzerland', 'IE':'Ireland',
                   'SE':'Sweden','PT':'Portugal','AT':'Austria','BE':'Belgium','EL':'Greece','FI':'Finland','LT':'Lithuania',
                   'LU':'Luxembourg','LV':'Latvia','SK':'Slovakia','NL':'Netherlands','IT':'Italy','DE':'Germany',
                   'FR':'France','SI':'Slovenia','HR':'Croatia'},inplace=True)
    #Changing Rows and Columns
    wp = pd.DataFrame(wp,index=[countries_list], columns=[years_list])



print(wp)