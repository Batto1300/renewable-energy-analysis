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
wind_prod["Mean Wind Production"] = wind_prod.mean(axis=1)

#Import Energy Consumption
energy_consumption = pd.read_csv(open(ENERGY_CONSUMPTION), index_col=0, decimal=',')
#Total wind production for each country from 2000-2015
energy_consumption["sum"] = energy_consumption.sum(axis=1)
#Join the two DataFrames together
joined_wind = wind_capacity.join(wind_prod["Mean Wind Production"], lsuffix='WC', rsuffix='WP')
#Plotting wind production/wind capacity
joined_wind.plot(x='Mean Wind Production', y='2015', kind='scatter')
plt.title('Correlation between wind capacity and wind production', pad=30)
plt.xlabel('Mean Wind Production')
plt.ylabel('Wind Capacity')
plt.grid()
plt.show()

