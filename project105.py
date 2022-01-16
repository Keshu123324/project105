import pandas as pd
import plotly.express as ps
import csv

with open('data105.csv',newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
data_file=0
total_entries=len(file_data)

for data in file_data:
    data_file+=float(data[1])

mean=data_file/total_entries

print("Mean is: "+str(mean))
