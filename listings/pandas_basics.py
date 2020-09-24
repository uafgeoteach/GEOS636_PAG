import numpy as np
import pandas as pd

s = pd.Series([23, 3, 2.3, 1, 2.3332], 
              index=['a', 'b', 'c', 'd', 'e'])

print("Series:")
print(s)

df = pd.DataFrame(np.random.randn(6, 4), 
              columns=['A', 'B', 'C', 'D'])

print("\nDataFrame:")
print(df)

