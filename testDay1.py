#!/usr/bin/python

import unittest
import day1
import numpy as np

class TestDay1(unittest.TestCase):

	def test_small(self):
		day1.main(np.array([1,2,1,2]))
		self.assertEqual(day1.getTotalSum(), 6);

	def test_self(self):
		day1.main(np.array([1,2,3,4,5,1,2,8,9,9]))
		self.assertEqual(day1.getTotalSum(), 6);

	def test_from_file(self):
		with open('inputDay1') as f:
			lines = f.readlines()
		for line in lines:
			array = np.fromstring(line, dtype=int, sep=',')
		
		day1.main(array)
		self.assertEqual(day1.getTotalSum(),1146)

if __name__ == '__main__':
	unittest.main()