import pandas as pd

#get a dataframe that uses the first column as index (index_col=0)
#and has a header line, and field separator is a whitespace ' '
stations = pd.read_csv('station.txt', sep=' ', header=0, index_col=0)

#print three stations we are interested in, using the index
#(isn't that easy?)
print(stations.loc[['ANMO', 'BAR', 'CL7']])
