import os

_absolute_path = os.path.dirname(os.path.abspath(__file__))
_adjusted_folders = _absolute_path.split(os.path.sep)[:-1]
_adjusted_folders.append('renewable_energy_analysis')
_adjusted_path = os.path.sep.join(_adjusted_folders)

class OriginalPaths:
    GDP = os.path.join(_adjusted_path, 'datasets', 'original', 'GDP_2010_constant.csv')
    POLITICS = os.path.join(_adjusted_path, 'datasets', 'original', 'CPDS_1960_2016_Update-2018.csv')
    CONSUMPTION = os.path.join(_adjusted_path, 'datasets', 'original', 'energy_consumption.csv')
    CAPACITY = os.path.join(_adjusted_path, 'datasets', 'original', 'all_energy_capacity.csv')
    WIND = os.path.join(_adjusted_path, 'datasets', 'original', 'wind_production.csv')

class CleanedPaths:
    GDP = os.path.join(_adjusted_path, 'datasets', 'cleaned', 'GDP_2010_constant.csv')
    POLITICS = os.path.join(_adjusted_path, 'datasets', 'cleaned', 'CPDS_1960_2016_Update-2018.csv')
    CONSUMPTION = os.path.join(_adjusted_path, 'datasets', 'cleaned', 'energy_consumption.csv')
    CAPACITY = os.path.join(_adjusted_path, 'datasets', 'cleaned', 'all_energy_capacity.csv')
    WIND = os.path.join(_adjusted_path, 'datasets', 'cleaned', 'wind_production.csv')
    COUNTRIES = os.path.join(_adjusted_path, 'datasets', 'cleaned', 'common_countries.csv')
    YEARS = os.path.join(_adjusted_path, 'datasets', 'cleaned', 'common_years.csv')