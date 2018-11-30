import pandas as pd
import matplotlib.pyplot as plt
import numpy.polynomial as poly
import file_names as fn

GDP_FILE = fn.CleanedPaths.GDP
ENERGY_CAPACITY_FILE = fn.CleanedPaths.CAPACITY
ENERGY_CONSUPTION_FILE = fn.CleanedPaths.CONSUMPTION

gdp = pd.read_csv(GDP_FILE, index_col = 0)
capacity = pd.read_csv(ENERGY_CAPACITY_FILE, index_col=0)
consumption = pd.read_csv(ENERGY_CONSUPTION_FILE,decimal=',',index_col=0)
capacity_reduced = capacity.drop('Technology',axis=1)
capacity_reduced = capacity.groupby('country').sum()
capacity_reduced = capacity_reduced.divide(consumption)
common_columns = [str(x) for x in range(2000, 2015)]
quantiles = []
gdp_capacity = gdp.join(capacity_reduced,lsuffix='x',rsuffix='y')
for i in range(2000, 2016):
    gdp_column_name = "{}x".format(str(i))
    capacity_column_name = "{}y".format(str(i))
    gdp_column = gdp_capacity[gdp_column_name]
    capacity_column = gdp_capacity[capacity_column_name]
    if gdp_column.any() and capacity_column.any():
        p = poly.Polynomial.fit(gdp_column, capacity_column,2)
        plt.figure(i)
        plt.plot(gdp_column, capacity_column,'o')
        plt.plot(*p.linspace())
plt.show()
