import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# get data file from command line
file = sys.argv[1]

print("plotting %s" % file)

# parse it with pandas

try:
    vel_data = pd.read_csv(file, parse_dates=True, index_col=0)
except:
    print("%s does not seem to be a CSV file" % file)
    exit()

# make a mask to get rid of unreasonably certain points
try:
    mask = vel_data["v_error [m/yr]"] > 25
except:
    print("%s does not seem to be a valid file" % file)
    exit()

# Naming logic
name = os.path.basename(file).replace(".csv", "")  # get rid of file extension
name = name.split("_")

western = name[0]
if(len(name) == 1):
    tlingit = None
elif(len(name) == 2):
    tlingit = name[1]
    # Expand E/W
    tlingit = tlingit.replace("E", ", East Tributary")
    tlingit = tlingit.replace("W", ", West Tributary")
else:
    print("%s does not seem to be a valid file name" % file)
    exit()

# make a plot
plt.figure(figsize=(8, 4), dpi=300)
plt.plot(vel_data["v [m/yr]"][mask], "k.")
plt.ylabel("Speed (m/yr)")
plt.xlabel("Year")

if(tlingit is None):
    plt.title("%s Glacier" % (western))
else:
    plt.title("%s Glacier (Tlingit Name: Sit' %s)" % (western, tlingit))

plt.ylim(0, 5000)
plt.xlim(pd.Timestamp("2014"), pd.Timestamp("2022.5"))
plt.grid(True, linestyle="--")

# save the plot
plt.savefig(os.path.basename(file).replace(".csv", ""))
