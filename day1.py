#!/usr/bin/python

import numpy as np
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def main(inputArray):
	global totalSum;
	totalSum = 0
	global arraysize, array, halfArrayIndex;
	array = inputArray
	arraysize = array.size
	halfArrayIndex = int(arraysize/2-1)
	calculate(0)
	pass


def calculate( index ):
	global totalSum;
	if arraysize == index :
		return array[halfArrayIndex];
	number = array[index]
	nextval = calculate(index+1)
	if number == nextval:
		totalSum = totalSum + number
	compareTo = index + halfArrayIndex
	return array[compareTo%arraysize]

def getTotalSum():
	return totalSum;

if __name__ == "__main__":
    main(sys.argv)
