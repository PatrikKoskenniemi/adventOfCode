#!/usr/bin/python

import numpy as np

sum = 0

def calculate( restOfArray ):
	global sum;
	if restOfArray.size == 0 :
		return;
	number = restOfArray[0]
	restOfArray = np.delete(restOfArray,0)
	#print(restOfArray)
	if number == calculate(restOfArray):
		sum = sum + number
	return number;

with open('inputDay1') as f:
	lines = f.readlines()
	for line in lines:
		array = np.fromstring(line, dtype=int, sep=',')

#array = np.array([1,1,2,2,3,4,1])
array = np.append(array,array[0])
#print(array)
calculate(array)

print(sum)



