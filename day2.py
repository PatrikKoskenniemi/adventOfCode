#!/usr/bin/python

import numpy as np
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def main(inputText):
	global result;
	result = 0

	for array in inputText:
		array = array.replace('\t', ' ');
		array = list(map(lambda x : int(x), array.split(' ')))
		result += (np.amax(array)-np.amin(array))
	pass

def getResult():
	return result;


if __name__ == "__main__":
    main(sys.argv)
