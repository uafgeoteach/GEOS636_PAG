import numpy as np
import timeit

#generate random data (1Mx1 entries)
a = np.random.rand(1000000,1)
b = 3.0

#time the runtime of the loop
start1 = timeit.default_timer()
for i in range(len(a)):
    a[i]=a[i]*3
stop1 = timeit.default_timer()

#time the runtime of the numpy operation
start2 = timeit.default_timer()
a = a*b
stop2 = timeit.default_timer()

#compare the two
print ("Time loop: %.5f s" % (stop1-start1))
print ("Time np  : %.5f s" % (stop2-start2))

