import pandas as pd
import file_names as fn 
import csv

# original data (csv file) - Political parties in power for EU countries
POLITCS_PATH= fn.OriginalPaths.POLITICS
# countries common to all datasets
COUNTRIES = fn.CleanedPaths.COUNTRIES
# years common to all datasets
YEARS = fn.CleanedPaths.YEARS
# name of new csv file to store the new cleaned and filtered dataset
C_POLITICS_PATH=fn.CleanedPaths.POLITICS


# filling first column as the years 
politics_df = pd.read_csv(open(POLITCS_PATH))
politics_df = politics_df[['year', 'country','gov_right1', 'gov_cent1', 'gov_left1' ]]
# mergeing counties
countries_df = pd.read_csv(open(COUNTRIES))
politics_df = pd.merge(politics_df,countries_df,on='country')
# print(politics_df)
# merging Years 
years_df = pd.read_csv(open(YEARS))
years_df.rename(columns={'years':'year'}, inplace=True)
politics_df = pd.merge(politics_df,years_df,on='year')
politics_df['year'] = politics_df['year'].astype(dtype=int) 
# print(politics_df)
politics_df.to_csv(C_POLITICS_PATH, index= False)
