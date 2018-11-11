import os

_ABS_PATH = os.path.dirname(os.path.abspath(__file__))

class OriginalPaths:
    GDP = os.path.join(_ABS_PATH, 'datasets', 'original', 'GDP_2010_constant.csv')
    POLITICS = os.path.join(_ABS_PATH, 'datasets', 'original', 'CPDS_1960_2016_Update-2018.csv')
    CONSUMPTION = os.path.join(_ABS_PATH, 'datasets', 'original', 'energy_consumption.csv')
    CAPACITY = os.path.join(_ABS_PATH, 'datasets', 'original', 'all_energy_capacity.csv')
    WIND = os.path.join(_ABS_PATH, 'datasets', 'original', 'wind_production.csv')

class CleanedPaths:
    GDP = os.path.join(_ABS_PATH, 'datasets', 'cleaned', 'GDP_2010_constant.csv')
    POLITICS = os.path.join(_ABS_PATH, 'datasets', 'cleaned', 'CPDS_1960_2016_Update-2018.csv')
    CONSUMPTION = os.path.join(_ABS_PATH, 'datasets', 'cleaned', 'energy_consumption.csv')
    CAPACITY = os.path.join(_ABS_PATH, 'datasets', 'cleaned', 'all_energy_capacity.csv')
    WIND = os.path.join(_ABS_PATH, 'datasets', 'cleaned', 'wind_production.csv')
    COUNTRIES = os.path.join(_ABS_PATH, 'datasets', 'cleaned', 'common_countries.csv')
    YEARS = os.path.join(_ABS_PATH, 'datasets', 'cleaned', 'common_years.csv')