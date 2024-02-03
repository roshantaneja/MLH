#!/usr/bin/env python3
import os
import absorb_cost
import happy
import basic_path
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)

class TestAbsorb(unittest.TestCase):
	def test_absorb_0(self):
		s1 = "he"
		s2 = "e"
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 1)

	def test_absorb_1(self):
		s1 = "hill"
		s2 = "hill"
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 0)

	def test_absorb_2(self):
		s1 = "silly"
		s2 = "hilly"
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 1)

	def test_absorb_3(self):
		s1 = "shrill"
		s2 = "hill"
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 2)

	def test_absorb_4(self):
		s1 = "color"
		s2 = "colour"
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 1)

	def test_absorb_5(self):
		s1 = "car"
		s2 = "boat"
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 3)

	def test_absorb_5(self):
		s1 = "frog"
		s2 = "apple"
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 5)

	def test_absorb_6(self):
		s1 = ""
		s2 = ""
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 0)

	def test_absorb_7(self):
		s1 = "apple"
		s2 = "pineapple"
		result = absorb_cost.costToAbsorb(s1, s2)
		self.assertEqual(result, 4)

class TestHappy(unittest.TestCase):

    def make_field(self, nrows, ncols, f):
        return {"nrows": nrows, "ncols": ncols,
                "smiles": tuple(tuple(f(r,c) for c in range(ncols)) for r in range(nrows))}

    def check_result(self, field, happiness, result):
        self.assertIsInstance(result, list, "path should be a list")
        self.assertEqual(field["ncols"], len(result), "path length incorrect")
        last = result[0]
        for c in range(1, field["ncols"]):
            self.assertTrue(last-1 <= result[c] <= last+1, "invalid path")
            last = result[c]
        self.assertEqual(happiness, sum(field["smiles"][result[c]][c] for c in range(field["ncols"])),
                         "not minimum sadness path")

    # path_to_happiness tests
    def test_path_to_happiness_01(self):
        # single column field
        field = {"nrows": 3, "ncols": 1, "smiles": ((5,), (6,), (4,))}
        happiness = 4
        result = happy.pathToHappiness(field["smiles"])
        self.assertTrue(result == [2])
        self.check_result(field, happiness, result)

    def test_path_to_happiness_02(self):
        # a two column field
        field = {"nrows": 3, "ncols": 2, "smiles": ((6, 25), (5, 2), (4, 35))}
        happiness = 6
        result = happy.pathToHappiness(field["smiles"])
        self.assertTrue(result == [2,1])
        self.check_result(field, happiness, result)

        # a two column field with two solution paths; either is fine
        field = {"nrows": 3, "ncols": 2, "smiles": ((4, 18), (6, 0), (4, 18))}
        happiness = 4
        result = happy.pathToHappiness(field["smiles"])
        self.assertTrue(result == [0,1] or result == [2,1])
        self.check_result(field, happiness, result)

    def test_path_to_happiness_03(self):
        # single row field
        field = {"nrows": 1, "ncols": 10, "smiles": ((5, 6, 4, 0, 5, 2, 1, 8, 9, 1),)}
        happiness = 41
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

    def test_path_to_happiness_04(self):
        # small size fields
        field = {"nrows": 2, "ncols": 3, "smiles": ((100, 3, 5), (2, 4, 6))}
        happiness = 10
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

        field = self.make_field(5, 3, lambda r, c: (r+c+2)%4)
        happiness = 0
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

        field = self.make_field(4, 5, lambda r, c: abs(r-2))
        happiness = 0
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

        field = self.make_field(5, 8, lambda r, c: 1 if r==c else 2)
        happiness = 11
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

    def test_path_to_happiness_05(self):
        # tall fields
        field = self.make_field(20, 5, lambda r, c: (r+c+3)%7+4)
        happiness = 20
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

        field = self.make_field(200, 4, lambda r, c: (r+c+3)%7+4)
        happiness = 16
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

    def test_path_to_happiness_06(self):
        # wide field with 2 rows
        field = self.make_field(2, 20, lambda r, c: (r+c+2)%4)
        happiness = 15
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

    def test_path_to_happiness_07(self):
        # wide field with 3 rows
        field = self.make_field(3, 15, lambda r, c: (r+c+2)%4)
        happiness = 6
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

    def test_path_to_happiness_08(self):
        # medium size fields
        field = self.make_field(17, 12, lambda r, c: (r+c)%7+1)
        happiness = 12
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

    def test_path_to_happiness_09(self):
        # large field
        field = self.make_field(47, 50, lambda r, c: (r*c+1)%7)
        happiness = 36
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

    def test_path_to_happiness_10(self):
        # larger field
        field =self.make_field(100, 200, lambda r, c: (r*c+r+c)%7)
        happiness = 311
        self.check_result(field, happiness, happy.pathToHappiness(field["smiles"]))

class TestBasic(unittest.TestCase):
	def test_basic_0(self):
		grid = [[0,1,0],[0,1,0],[0,1,0]]
		result = basic_path.findPath(grid)
		self.assertIsInstance(result, list, "path should be a list")
		self.assertEqual(len(result), len(grid), "path is not correct length")
		self.assertTrue(result[0][0]==0, "path does not start at top of grid")
		self.assertTrue(result[len(result)-1][0]==len(grid)-1, "path does not end at bottom of grid")
		self.assertEqual(result, [(0,1),(1,1),(2,1)], "path is incorrect")

	def test_basic_1(self):
		grid = [[0,0,0,1],[0,1,1,1],[1,0,0,0]]
		result = basic_path.findPath(grid)
		self.assertEqual(result, None)

	def test_basic_2(self):
		grid = [[1,0,0,1],[0,1,1,1],[1,0,0,0]]
		result = basic_path.findPath(grid)
		self.assertIsInstance(result, list, "path should be a list")
		self.assertEqual(len(result), len(grid), "path is not correct length")
		self.assertTrue(result[0][0]==0, "path does not start at top of grid")
		self.assertTrue(result[len(result)-1][0]==len(grid)-1, "path does not end at bottom of grid")
		self.assertEqual(result, [(0,0),(1,1),(2,0)], "path is incorrect")

	def test_basic_3(self):
		grid = [[0,1,0,1],[1,0,0,1],[0,1,0,1],[0,0,1,0],[0,1,0,0]]
		result = basic_path.findPath(grid)
		self.assertIsInstance(result, list, "path should be a list")
		self.assertEqual(len(result), len(grid), "path is not correct length")
		self.assertTrue(result[0][0]==0, "path does not start at top of grid")
		self.assertTrue(result[len(result)-1][0]==len(grid)-1, "path does not end at bottom of grid")
		option1 = result == [(0,3),(1,3),(2,3),(3,2),(4,1)]
		option2 = result == [(0,1),(1,0),(2,1),(3,2),(4,1)] 
		self.assertTrue(option1 or option2, "path is incorrect")

	def test_basic_4(self):
		grid = [[0,1,0,1,0],[1,0,0,1,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1]]
		result = basic_path.findPath(grid)
		self.assertEqual(result, None)

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
