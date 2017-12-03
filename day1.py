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

#array = np.array([1,1,2,2,3,4,1])
array = np.append(array,array[0])
arraysize = array.size

def calculate( index ):
#	print(index)
	global sum;
	#global array;
	if arraysize == index :
		return;
	number = array[index]
	#restOfArray = np.delete(restOfArray,0)
	#print(restOfArray)
	if number == calculate(index+1):
		sum = sum + number
	return number;

#print(array)
calculate(0)

print(sum)



