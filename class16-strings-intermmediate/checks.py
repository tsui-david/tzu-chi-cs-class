import unittest
from answers import *

class CheckDrills(unittest.TestCase):
    def test_check1(self):
        self.assertEqual("hel", ex1("hello"))

    def test_check2(self):
        self.assertEqual("llo mr. david", ex2("hello mr. david"))

    def test_check3(self):
        a = "hello"
        resp = ex3(a)
        self.assertEqual(resp, ex3(a))

    def test_check4(self):
        self.assertEqual("ate", ex4(" asdfsdf plate"))
    
    def test_check5(self):
        self.assertEqual(True, ex5("hi", "hi"))
        self.assertEqual(False, ex5("df", "fd"))

    def test_check6(self):
        self.assertEqual("abcde", ex6("ace", "bd"))

if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()