import pandas as pd

#get a dataframe that uses the first column as index (index_col=0)
#and has a header line, and field separator is a whitespace ' '
stations = pd.read_csv('station.txt', sep=' ', header=0, index_col=0)

#select a subset of stations
new_stations = stations.loc[['ANMO', 'BAR', 'CL7']]

#write it to a new file
new_stations.to_csv('stations_short.csv')

