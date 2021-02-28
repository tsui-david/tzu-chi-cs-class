import unittest
from drills import *

class CheckDrills(unittest.TestCase):
    def test_check1(self):
        self.assertEqual("hello", ex1())

    def test_check2(self):
        self.assertEqual("hello mr. david", ex2(["hello", "mr.", "david"]))

    def test_check3(self):
        self.assertEqual(('c', 'd'), ex3('class dismissed'))

    def test_check4(self):
        self.assertEqual("ate", ex4("watermelon", 1, 4))
    
    def test_check5(self):
        self.assertEqual(True, ex5("ater", "watermelon"))
        self.assertEqual(False, ex5("xxx", "watermelon"))

    def test_check6(self):
        self.assertEqual("a*b*c", ex6("abc"))


    def test_check7(self):
        self.assertEqual("abcde", ex7("ace", "bd"))

if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()