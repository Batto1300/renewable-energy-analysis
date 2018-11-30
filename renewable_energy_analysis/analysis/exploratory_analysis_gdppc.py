import pandas as pd
import matplotlib.pyplot as plt
import numpy.polynomial as poly
import file_names as fn

ENTER_MSG = "Enter 1 for GDP and 2 for GDPPC"
GDP_FILE = fn.CleanedPaths.GDP
GDPPC_FILE = fn.CleanedPaths.GDPPC
ENERGY_CAPACITY_FILE = fn.CleanedPaths.CAPACITY
ENERGY_CONSUPTION_FILE = fn.CleanedPaths.CONSUMPTION

def plot_all_years(dataframe, normalize=True):
        capacity = pd.read_csv(ENERGY_CAPACITY_FILE, index_col=0)
        capacity_reduced = capacity.drop('Technology',axis=1)
        capacity_reduced = capacity.groupby('country').sum()
        if normalize:
                consumption = pd.read_csv(ENERGY_CONSUPTION_FILE,decimal=',',index_col=0)
                capacity_reduced = capacity_reduced.divide(consumption)
        df_capacity = dataframe.join(capacity_reduced,lsuffix='x',rsuffix='y')
        for i in range(2000, 2016):
                metric_column_name = "{}x".format(str(i))
                capacity_column_name = "{}y".format(str(i))
                metric_column = df_capacity[metric_column_name]
                capacity_column = df_capacity[capacity_column_name]
                if metric_column.any() and capacity_column.any():
                        p = poly.Polynomial.fit(metric_column, capacity_column,2)
                        plt.figure(i)
                        plt.plot(metric_column, capacity_column,'o')
                        plt.plot(*p.linspace())
        plt.show()

if __name__ == '__main__':
        input_ = input(ENTER_MSG)
        if input_ == '1':
                gdp = pd.read_csv(GDP_FILE, index_col = 0)
                plot_all_years(gdp)
        if input_ == '2':
                gdppc = pd.read_csv(GDPPC_FILE, index_col = 0)
                plot_all_years(gdppc, normalize=False)
