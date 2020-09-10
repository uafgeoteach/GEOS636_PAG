# for variable in sequence 
#   STATEMENT
# 
# EXAMPLE: countingm adding
#

import numpy as np

for x in range(11):
    if x == 2:
        print("Two is prime!")
        continue
    
    if x == 5:
        print("I'll stop")
        break

    print("x = %d" % x)


   
