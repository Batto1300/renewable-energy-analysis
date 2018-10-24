# Renewable Energy Analysis
Representing and Manipulating Data - Univeristy of Stirling Course Project


## Instructions on how to clean the datasets

1. Remove the unused columns
2. Set the column as : Nation, Year1, Year2,..., YearX
3. If only have the Nation code, join your dataset with another that has also the Nation name 
4. Filter out the Nations by joining with the Nation List (Nation List to be created yet)
5. Set the row-index on Nation, Set a multilevel index on Year1, Year2,..., YearX called as the DataFrame
6. Save the dataset on the adjusted folder

Also:
* Do __not__ touch the datasets in the original folder, just open them in read mode.
* Remember to keep only the columns in point 2. because you will add columns to the dataframe as you join.
* The script must be named _datasetname_cleaning.py_ e.g.: _Latitude_cleaning.py_ and placed in the top level of the dataset folder.
