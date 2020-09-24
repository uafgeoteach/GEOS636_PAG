import numpy as np

#create an ndarray
data = np.array([4,9,16,25])

#calculate the sum of the elements 
#(call the function sum() on the OBJECT
#data)
print("sum=", data.sum())

#calculate sqrt, hand data to 
#numpy function
print("sqrt=", np.sqrt(data))

#calculate vector norm: norm = sqrt(sum(x(i)^2))
print("norm=",np.linalg.norm(data))
