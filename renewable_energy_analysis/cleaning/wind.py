import file_names as fn
import country_converter as cc
import pandas as pd

WIND_PATH = fn.OriginalPaths.WIND
C_WIND_PATH = fn.CleanedPaths.WIND
YEARS_PATH = fn.CleanedPaths.YEARS


pd.set_option('display.width', 5000)
pd.set_option('max.columns', 5000)

wp = pd.read_csv(open(WIND_PATH))
years_list = open(YEARS_PATH).readlines()[1:]
years_list = list(map(lambda x: int(x[:-1]),years_list))

wp = wp[wp['Year'].isin(years_list)]

print(wp)