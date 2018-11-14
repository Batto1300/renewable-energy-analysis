# Renewable Energy Analysis - Representing and Manipulating Data - Univeristy of Stirling Course Project

## Before Writing the code

1. From the project root folder: `pip install -r requirements.txt`
2. Add the project folder to the PYTHONPATH.
3. To check that you addded it corectly run pytest from the project folder

Usefull Links:

* [PYTHONPATH Mac](https://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath)
* [PYTHONPATH Windows](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows)

## Instructions on how to access the datasets

To access the datasets import the renewable_energy_analysis package and access the paths like so:

```python
import renewable_energy_analysis as rea
# access original files
# use always r (read)
gdp_file = open(rea.OriginalPaths.GDP,'r')
```

or

```python
import renewable_energy_analysis as rea
# access cleaned files
# use r (read) or w (write) depending on the use
gdp_file = open(rea.CleanedPaths.GDP, 'r')
```

## Instructions on how to clean the datasets

1. Remove the unused columns
2. Set the column as : Nation, Year1, Year2,..., YearX
3. If only have the Nation code, join your dataset with another that has also the Nation name
4. Filter out the Nations by joining with the nation list (datasets/cleaned/common_countries).
5. Filter out the Years by joining with the year list (datasets/cleaned/common_years).
6. Set the row-index on Nation, Set a multilevel index on Year1, Year2,..., YearX called as the DataFrame
7. Save the dataset on the cleaned folder

Also:

* Remember to keep only the columns in point 2. because you will add columns to the dataframe as you join.
* The script must be named _datasetname_cleaning.py_ e.g.: _Latitude_cleaning.py_ and placed in the renewable_enrgy_analysis/cleaning folder.
