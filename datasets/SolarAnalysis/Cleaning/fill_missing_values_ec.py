import pandas as pd
import os
import csv
import seaborn as sns
import matplotlib.pyplot as plt

FILENAME = "original_data.csv"
OUTPUT_FILENAME = "all_energy_capacity.csv"


with open(FILENAME, 'r') as o, open(OUTPUT_FILENAME, "w") as w:  
    nation_reader = csv.reader(o)
    header = next(nation_reader)
    w.write("{}\n".format(','.join(header)))
    row = next(nation_reader)
    while row:
        for i in range(3):
            if i == 0:
                country = row[0]
            else:
                row[0] = country
            w.write("{}\n".format(','.join(row)))
            try:
                row = next(nation_reader)
            except StopIteration:
                row = None   # empty address

