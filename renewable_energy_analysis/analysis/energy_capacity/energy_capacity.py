import file_names as fn
import pandas as pd 
import matplotlib.pyplot as plt
import os

# import energy capacity
ENERGY_CAPACITY = fn.CleanedPaths.CAPACITY


energy_capacity = pd.read_csv(ENERGY_CAPACITY)
energy_capacity_sum = energy_capacity.groupby("country").sum()
energy_capacity_sum["2015"] = energy_capacity_sum["2015"]/energy_capacity_sum["2015"].sum() * 100
# cumulative wind, hydro, solar energy capacity as of 2015 - ascending order
energy_capacity_sum["2015"].sort_values(ascending = False).plot.bar()
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