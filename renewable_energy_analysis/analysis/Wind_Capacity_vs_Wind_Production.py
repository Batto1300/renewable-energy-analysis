import file_names as fn
import pandas as pd
import matplotlib.pyplot as plt

#Pandas Settings
pd.set_option('display.width', 2000)
pd.set_option('max.columns', 2000)

#File Paths
WIND_PRODUCTION = fn.CleanedPaths.WIND
ENERGY_CAPACITY = fn.CleanedPaths.CAPACITY
ENERGY_CONSUMPTION = fn.CleanedPaths.CONSUMPTION

#Import all energy capacity DF
energy_capacity = pd.read_csv(open(ENERGY_CAPACITY), index_col=0)
#Filter Energy Capacity to Wind Related Data Only
wind_capacity = energy_capacity[energy_capacity['Technology'] == 'Wind']
#Import Wind Production DF
wind_prod = pd.read_csv(open(WIND_PRODUCTION), index_col=0)
#Import Energy Consumption
energy_consumption = pd.read_csv(open(ENERGY_CONSUMPTION), index_col=0, decimal=',')
#Total wind production for each country from 2000-2015
energy_consumption["sum"] = energy_consumption.sum(axis=1)
#Join the two DataFrames together
joined_wind = wind_capacity.join(energy_consumption, lsuffix='WC', rsuffix='WP')

#Joining wind production with joined wind capacity and energy consumption
joined_energy = wind_prod.join(joined_wind)
#Creating Bins
bin_range = (joined_energy['sum'].max() - joined_energy['sum'].min())/3
next_bin = joined_energy['sum'].min()
bins = []
bins.append(next_bin)
for _ in range(1,4):
        next_bin += bin_range
        bins.append(next_bin)
bins[0]+=-1
joined_energy['binned'] = pd.cut(joined_energy['sum'], bins, labels=['low','medium','high'])
#Creating scatter plot
joined_energy[joined_energy['binned'] == 'low'].plot(x='2015WP',y='2015WC', kind='scatter')
plt.show()
print(joined_energy)




