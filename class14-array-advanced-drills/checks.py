import unittest
# from drills import *
from answers import *

class CheckDrills(unittest.TestCase):
  def test_ex1(self):
    ans = ex1([3, -1, 2])
    self.assertEqual(ans, 1)
  
  def test_ex2(self):
    ans = ex2(["totally", "cool"], "cool")
    self.assertEqual(ans, 1)

    ans = ex2(["totally", "cool"], "bad")
    self.assertEqual(ans, -1)
  
  def test_ex3(self):
    ans = ex3(["t", "a", "b", "a", "b"], "b")
    self.assertEqual(ans, [2,4])

    ans = ex3(["t", "a"], "b")
    self.assertEqual(ans, [])
  
  def test_ex4(self):
    ans = ex4([1,2,3,4], 4)
    self.assertEqual(ans, (1,3))

    ans = ex4([1,2,3,4], 100)
    self.assertEqual(ans, None)
  
  def test_ex5(self):
    ans = ex5([1,2,3,4], 5)
    self.assertEqual(sorted(ans), sorted([(1,4), (2,3)]))

    ans = ex5([1,2,3,4], 100)
    self.assertEqual(ans, [])
  
  def test_ex6(self):
    ans = ex6([1,2,3,4,5], 5)
    self.assertEqual(sorted(ans), sorted([(1,4), (2,3), tuple([5])]))

    ans = ex6([1,2,3,4,5], 100)
    self.assertEqual(ans, [])
  
  def test_ex7(self):
    ans = ex7(["O", "X"])
    self.assertFalse(ans)

    ans = ex7(["O", "O"])
    self.assertTrue(ans)

    ans = ex7([])
    self.assertTrue(ans)

    ans = ex7(["X"])
    self.assertTrue(ans)

  def test_ex8(self):
    ans = ex8([["X", "X"], ["X", "O"]])
    self.assertTrue(ans)

    ans = ex8([["X", "O"], ["O", "X"]])
    self.assertFalse(ans)
  
if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()