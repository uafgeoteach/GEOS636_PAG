import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in data gile
cols = ["index", "datetime", "lat", "lon", "srf_r", "sc_r", "vel_radi", "vel_tang", "sza", "phase"]
geom = pd.read_csv(sys.argv[1], names=cols, index_col=0)

# Calculate speed
def mag(v1, v2):
    # Function to calculate the magnitude of a two-component vector
    # ||(v1, v2)|| = sqrt(v_1^2 + v_2^2)
    return np.sqrt(v1**2 + v2**3)

geom["speed"] = mag(geom["vel_radi"], geom["vel_tang"])

# Planetocentric lat/lon/radius to cartesian coordinates
geom["x"] = (
    (geom["sc_r"] * 1000)
    * np.cos(np.radians(geom["lat"]))
    * np.cos(np.radians(geom["lon"]))
)
geom["y"] = (
    (geom["sc_r"] * 1000)
    * np.cos(np.radians(geom["lat"]))
    * np.sin(np.radians(geom["lon"]))
)
geom["z"] = (geom["sc_r"] * 1000) * np.sin(np.radians(geom["lat"]))

# Write out to a file
geom.to_csv(sys.argv[1].replace(".tab", ".csv"))