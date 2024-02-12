#!/usr/bin/env python3
import os
import frog_hops
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)

class TestFrog(unittest.TestCase):
	def check_result(self, home, result):
		self.assertIsInstance(result, list, "path should be a list")
		self.assertTrue(result[0]==0, "missing start")
		self.assertTrue(result[-1]==home, "missing end")
		run=1
		for i in range(len(result)-1):
			self.assertTrue(result[i+1]-result[i]-run<=1)
			run=result[i+1]-result[i]

	def test_frog_0(self):
		home = 10
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==5)
		self.check_result(home, result)

	def test_frog_1(self):
		home = 1
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==2)
		self.check_result(home, result)

	def test_frog_2(self):
		home = 37
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==10)
		self.check_result(home, result)

	def test_frog_3(self):
		home = 40
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==10)
		self.check_result(home, result)

	def test_frog_4(self):
		home = 100
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==15)
		self.check_result(home, result)

	def test_frog_5(self):
		home = 562
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==35)
		self.check_result(home, result)

	def test_frog_6(self):
		home = 1000
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==46)
		self.check_result(home, result)

	def test_frog_7(self):
		home = 8402
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==131)
		self.check_result(home, result)

	def test_frog_8(self):
		home = 10000
		result = frog_hops.getMinHoppingPath(home)
		self.assertTrue(len(result)==142)
		self.check_result(home, result)

	# this one takes a bit too long to run!
	# def test_frog_6(self):
	# 	home = 20000
	# 	result = frog_hops.getMinHoppingPath(home)
	# 	self.assertTrue(len(result)==201)
	# 	self.check_result(home, result)

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)