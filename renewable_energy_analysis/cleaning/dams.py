import pandas as pd
import file_names as fn

DAMS_PATH = fn.OriginalPaths.DAMS
CLEAN_DAMS_PATH = fn.CleanedPaths.DAMS
COUNTRY_PATH = fn.CleanedPaths.COUNTRIES
COUNTRIES_COL = 'country'


dams_df = pd.read_csv(open(DAMS_PATH))
country_df = pd.read_csv(open(COUNTRY_PATH))
dams_df = pd.merge(dams_df,country_df,on = COUNTRIES_COL)
dams_df.to_csv(CLEAN_DAMS_PATH,index=False)