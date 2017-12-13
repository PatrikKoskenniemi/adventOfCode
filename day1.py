#!/usr/bin/python

import numpy as np
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

sum = 0
with open('inputDay1') as f:
	lines = f.readlines()
	for line in lines:
		array = np.fromstring(line, dtype=int, sep=',')

#array = np.array([1,2,3,4,5,1,2,8,9,9])
#array = np.array([1,2,1,2])
arraysize = array.size
halfArrayIndex = int(arraysize/2-1)

def calculate( index ):
	global sum;
	if arraysize == index :
		return array[halfArrayIndex];
	number = array[index]
	nextval = calculate(index+1)
	if number == nextval:
		sum = sum + number
	compareTo = index + halfArrayIndex
	return array[compareTo%arraysize]

calculate(0)

print("sum: " + str(sum))



