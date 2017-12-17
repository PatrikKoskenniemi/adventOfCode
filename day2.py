#!/usr/bin/python

import numpy as np
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def main(inputText):
	global result;
	result = int(0)

	for array in inputText:
		array = array.replace('\t', ' ');
		array = list(map(lambda x : int(x), array.split(' ')))
		for currentPos,currentVal in enumerate(array):
			for nextPos,nextVal in enumerate(array):
				if( currentVal%nextVal == 0 and (currentPos != nextPos)):
					result += int(currentVal/nextVal)
				pass
			pass
		pass
	pass

def getResult():
	return result;


if __name__ == "__main__":
    main(sys.argv)
