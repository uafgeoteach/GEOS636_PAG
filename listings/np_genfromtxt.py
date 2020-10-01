import numpy as np

#Uses the header line to name 
#the output field via "names=True"
stations = np.genfromtxt('station.txt', 
			  encoding='utf-8', 
			  dtype=None, 
			  delimiter=' ', 
			  names=True)

#what did you get back?
print(stations)

#what are the column names?
print(stations.dtype.names)

#get all station names
print(stations['Name'])

#get all station latitudes
print(stations['Lat'])
