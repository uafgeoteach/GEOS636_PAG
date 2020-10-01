import numpy as np

#Uses the header line to name the output variables, using "names=True"
stations = np.genfromtxt('station.txt', encoding='utf-8', 
			  dtype=None, delimiter=' ', names=True)

#delete all but the first three entries
stations = np.delete(stations, range(3,len(stations)), 0)

np.savetxt('stations_short.txt', stations, fmt='%s %f %f %i %i %i')

