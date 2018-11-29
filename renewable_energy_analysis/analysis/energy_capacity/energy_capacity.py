import file_names as fn
import pandas as pd 
import matplotlib.pyplot as plt
import os


# import energy capacity
ENERGY_CAPACITY = fn.CleanedPaths.CAPACITY
COUNTRY_COLUMN = "country"


df_energy_capacity = pd.read_csv(ENERGY_CAPACITY)
df_energy_capacity_sum = df_energy_capacity.groupby(COUNTRY_COLUMN).sum()
df_energy_capacity_sum["2015"] = df_energy_capacity_sum["2015"]/df_energy_capacity_sum["2015"].sum() * 100
# cumulative wind, hydro, solar energy capacity as of 2015 - ascending order
df_energy_capacity_sum["2015"].sort_values(ascending = False).plot.bar()
# title
plt.title("% Total Europe Renewable Energy Capacity 2015: \n Solar, Wind, Hydro", pad=30)
# ylabel
plt.ylabel("% Total Europe 2015 Capacity (MW)")
plt.tight_layout()
plt.ylim((0,30))
# save graph
plt.savefig(os.path.join(fn._adjusted_path, 'analysis', 'energy_capacity' ,'all_energy_capacity_country_2015.png'))
# close window
plt.close("all")
# Europe Renewable Energy Capacity in time
df_energy_capacity_europe = df_energy_capacity.sum(axis = 0)[2:]
df_energy_capacity_europe_growth = df_energy_capacity_europe.pct_change()*100
plt.plot(df_energy_capacity_europe_growth, ls = "dashed", linewidth=3.0)
# title
plt.title("% Growth Total Europe Renewable Energy Capacity: \n Solar, Wind, Hydro", pad=30)
# ylabel
plt.ylabel("% Growth (MW)")
plt.xticks(rotation=45)
plt.ylim((0,14))
#plt.style.use('classic')
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(fn._adjusted_path, 'analysis', 'energy_capacity' ,'all_energy_capacity_time.png'))
plt.close("all")