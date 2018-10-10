import pandas as pd 


# PANDAS DATAFRAME CONCATENATE, MERGE, JOIN

# concatenate: appends dataframe to other dataframe either 
# at column or row 

# merge: 
# - inner: maintains only those values whose on = "" values appear 
# in both datasets - intersection
# - outer: mantains all values - union
# left: maintains all values according to dataframe
# right



filenames = ["all_energy_capacity.csv", "GDPPC-2010-constant.csv"]

list_of_df = [pd.read_csv(filename) for filename in filenames]

# append dataset to the other maintaining only countries that 
# appear in both datasets 
#bigdata = pd.merge(list_of_df[0].reset_index(), list_of_df[1], on = ["country"], how = "inner")

#newdf = pd.merge(energy.reset_index(), ScimEn, on='Country').merge(GDP.reset_index(), on='Country')

df = pd.concat(list_of_df, axis = 0)

with pd.option_context('display.max_rows', None, 'display.max_columns', df.shape[1]):
    print(df)