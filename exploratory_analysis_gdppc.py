# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy.polynomial as poly

GDP_FILE = 'datasets/adjusted/GDP-2010-constant.csv'
ENERGY_CAPACITY = 'datasets/all_energy_capacity.csv'

gdp = pd.read_csv(GDP_FILE)
# %%
capacity = pd.read_csv(ENERGY_CAPACITY)
capacity = capacity[capacity.Technology.str.contains('Wind')]
common_columns = [str(x) for x in range(2000, 2017)] + ['country']
gdp_reduced = gdp[common_columns]
capacity_reduced = capacity[common_columns]
quantiles = []
gdp_capacity = pd.merge(gdp_reduced, capacity_reduced, on='country')
for column in gdp_capacity.columns.tolist():
    if column != 'country':
        column_values = gdp_capacity[column]
        q1 = column_values.quantile(q=0.25)
        q3 = column_values.quantile(q=0.75)
        iqr = q3 - q1
        quantiles.append((column,q1,q3,iqr))
        gdp_capacity = gdp_capacity[gdp_capacity[column] < (iqr * 3)]

for i in range(2003, 2017):
    gdp_column_name = "{}_x".format(str(i))
    capacity_column_name = "{}_y".format(str(i))
    gdp_column = gdp_capacity[gdp_column_name]
    capacity_column = gdp_capacity[capacity_column_name]
    if gdp_column.any() and capacity_column.any():
        p = poly.Polynomial.fit(gdp_column, capacity_column,2)
        plt.figure(i)
        plt.plot(gdp_column, capacity_column,'o')
        plt.plot(*p.linspace())
plt.show()