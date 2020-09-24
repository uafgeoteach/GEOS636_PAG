import pandas as pd
import numpy as np

#we want 10 data
num_data = 10

#create 10 days starting on the day 
#this lecture is published
index = pd.date_range('09/24/2020', 
                periods=num_data)

#make the (random) data frame of
#num_data rows and 3 colums labled 
#north, east and vertical; 
#indexed by the time series created above
df=pd.DataFrame(np.random.randn(num_data, 3), 
        index=index, 
        columns=('North', 'East', 'Vertical'))

print(df)

#print summary statistics
print(df.describe())
