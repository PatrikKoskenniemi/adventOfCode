#!/usr/bin/python

import unittest
import numpy as np
import day2

class testDay2(unittest.TestCase):

	def test_example(self):
		array =["5 9 2 8","9 4 7 3","3 8 6 5"]
		day2.main(array)
		self.assertEqual(day2.getResult(), 9)

	def test_real(self):
		with open('inputDay2') as f:
			lines = f.readlines()
			day2.main(lines)

		self.assertEqual(day2.getResult(), 53460)

if __name__ == '__main__':
	unittest.main()