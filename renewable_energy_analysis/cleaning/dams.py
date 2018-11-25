#importing packages
import pandas as pd
import file_names as fn
#defining constants
DAMS_PATH = fn.OriginalPaths.DAMS
CLEAN_DAMS_PATH = fn.CleanedPaths.DAMS
COUNTRY_PATH = fn.CleanedPaths.COUNTRIES
COUNTRIES_COL = 'country'

#opening two dataframes
dams_df = pd.read_csv(open(DAMS_PATH))
country_df = pd.read_csv(open(COUNTRY_PATH))
#merging the two dataframes by index 0
dams_df = pd.merge(dams_df,country_df,on = COUNTRIES_COL)
#saving the new data frame
dams_df.to_csv(CLEAN_DAMS_PATH,index=False)