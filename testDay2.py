#!/usr/bin/python

import unittest
import numpy as np
import day2

class testDay2(unittest.TestCase):

	def test_example(self):
		array =["5 1 9 5","7 5 3","2 4 6 8"]
		day2.main(array)
		self.assertEqual(day2.getResult(), 18)

	def test_read_from_bad_text(self):
		badText = "1 2\t3 4"
		badText = badText.replace('\t', ' ')
		self.assertEqual(badText, "1 2 3 4")
		goodArray = np.fromstring(badText, dtype=int, sep=' ')
		self.assertEqual(goodArray.all(), np.array([1,2,3,4]).all())

	def test_real(self):
		with open('inputDay2') as f:
			lines = f.readlines()
			day2.main(lines)

		self.assertEqual(day2.getResult(), 53460)

if __name__ == '__main__':
	unittest.main()