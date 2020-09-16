# for variable in sequence 
#   STATEMENT
# 
# EXAMPLE: countingm adding
#

import numpy as np

#from 2 to 10 in steps of 2
for x in range(2,11,2):
    print(x)
print("first `for' done\n")

#sum of vector elements
s = 0
for x in np.array([23,1,5]):
   s = s + x    

print(s)
