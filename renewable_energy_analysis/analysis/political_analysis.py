import file_names as fn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

POLITCS_PATH = fn.CleanedPaths.POLITICS
CAPACITY_PATH = fn.CleanedPaths.CAPACITY
LABEL_MAP = {'gov_right1': 'right','gov_cent1':'center','gov_left1':'left'}


politics = pd.read_csv(POLITCS_PATH)
# calculate difference, drop first column and move years to rows.
years = [str(x) for x in range(2000,2016)]
capacity = pd.read_csv(CAPACITY_PATH).groupby('country',as_index = False).sum()
capacity[years] = capacity[years].diff(axis=1)
capacity.drop(columns=['2000'],inplace=True)
capacity = pd.melt(capacity, id_vars='country',var_name='year',value_name='capacity')
capacity['year'] = capacity['year'].astype(dtype=int)
#merge on country and year
pol_cap = pd.merge(politics,capacity,on=['country','year'],how='inner')
#calculate orientation column
new_indexes = []
new_values = []
for index, row in pol_cap[['gov_right1','gov_cent1','gov_left1']].iterrows():
        percentages = [row['gov_right1'] , row['gov_left1'], row['gov_cent1']]
        max_ = max(percentages)
        count = 0
        for item in row.iteritems():
            if item[1] == max_:
                #append name of the column tranformed
                count += 1
                if count < 2:
                    new_values.append(LABEL_MAP[item[0]])
                    new_indexes.append(index)
#create new dataset and join it to the original, drop already used columns
pol_cap.drop(columns=['gov_right1','gov_cent1','gov_left1'],inplace=True)
new_df = pd.DataFrame(data=new_values,index=new_indexes,columns=['orientation'])
pol_cap = pol_cap.join(new_df)
#declare structures to create dataframe for capacity orientation means
new_columns = {"left":[],'center':[],'right':[], 'country':[]}
#calculate mean for every country orientation
pol_cap['year'] = pol_cap['year'].astype(float)
for country in pol_cap['country'].unique():
    new_columns['country'].append(country)
    #filter out data to leave just one country
    country_data = pol_cap[pol_cap['country'] == country]
    # https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
    country_data.is_copy = False
    country_data['capacity'] = country_data['capacity']/pd.Series(np.log(country_data['year']-2000.5))
    for orientation in pol_cap['orientation'].unique():
        new_mean = country_data[country_data['orientation'] == orientation].mean(axis=0)[1]
        new_columns[orientation].append(new_mean)
means = pd.DataFrame(data=new_columns, columns=new_columns.keys())
print(means['right'].mean())
print(means['left'].mean())