import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILENAME = "all_energy_capacity_eu_percentage.csv"

df = pd.read_csv(FILENAME, index_col=[0, 1])

# Exploratory analysis #
# Compute average change in electric capacity per year per country

avg_change_el_cap_time = {}
countries = ["Europe", "Germany", "Italy", "Spain", "France"]
for i in countries:
    avg_change_el_cap_time[i] = list(df.loc[i, "2001":"2017"].sum(axis=0))


plt.figure(figsize=(10, 5))
sns.set_style("darkgrid")
time = list(df.columns[2:])
for key, value in avg_change_el_cap_time.items():
    plt.plot(time, list(value), label=key, linewidth = 1.9)

plt.legend()
plt.xlabel("Time")
plt.ylabel("Electric Capacity (MW)")
plt.title("Growth Rate In Electric Capacity - Solar, Wind, Hydropower")
plt.xticks(rotation=45)
plt.show()


# to autoformat style : shift command P format
