import pandas as pd
import file_names as fn
import matplotlib.pyplot as plt

CLEAN_DAMS_PATH = fn.CleanedPaths.DAMS
ENERGY_CAPACITY = fn.CleanedPaths.CAPACITY


dams_df = pd.read_csv(open(CLEAN_DAMS_PATH),index_col=0 )
capacity_df = pd.read_csv(ENERGY_CAPACITY, index_col=0)
capacity_df = capacity_df['2015']
dams_capactiy = dams_df.join(capacity_df)

ax = dams_capactiy.plot.scatter(x='number', y='2015')
ax.set(xlabel="Number of Dams", ylabel="Hydroelectric Energy Capacity (MW)")
plt.grid()
plt.title("Hydroelectric Energy vs Number Of Dams", pad = 30)
plt.show()