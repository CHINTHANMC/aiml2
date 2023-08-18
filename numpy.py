#numpy array
import numpy as np
arr=np.array((1,2,3))
print("dimension",arr.ndim)
print("shape of array",arr.shape)
print("dat type of array",arr.dtype)
print("size of array",arr.size)

#creating array with particular elements
arr=np.full((2,3),5)
print(arr)

#creating with zeroes
arr=np.zeros((2,3))
print(arr)

#creating with random numbers
arr=np.random.randint(low=1,high=100,size=(2,3))
print(arr)
