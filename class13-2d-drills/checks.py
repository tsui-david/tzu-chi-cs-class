import unittest
from exercises import *

class CheckDrills(unittest.TestCase):
    def test_example(self):
        ans = example()
        self.assertEqual(ans, 'wow!')

    def test_check1(self):
        arr = [[1,2,3,4],[5,6,7,8]]
        self.assertEqual(ex1(arr), [1,2,3,4])
    
    def test_check2(self):
      arr = [[1,2,3,4],[5,6,7,8]]
      ans = ex2(arr, 1)
      self.assertEqual(ans, [5,6,7,8])

    def test_check3(self):
      arr = [[1,2,3,4],[5,6,7,8]]
      ans = ex3(arr, 1, 2)
      self.assertEqual(ans, 7)

    def test_check4_a(self):
      a = [[1,2,3]]
      ans = ex4_a(a)
      a = [[1,2,4]]
      self.assertIsNot(a, ans)
      self.assertEqual(ans, [[1,2,3]])
    
    def test_check4_b(self):
      a = [[[1,2,3]]]
      ans = ex4_b(a)
      a = [[[1,2,4]]]

      self.assertIsNot(a, ans)
      self.assertEqual(ans, [[[1,2,3]]])

    def test_check4(self):
      ans = ex4(3)
      self.assertEqual(ans, [['x', 'x', 'x'], ['*','*','*'],['x','x','x']])

    def test_check5(self):
      ans = ex5(3)
      self.assertEqual(ans, [['x', '*', 'x'], ['x','*','x'],['x','*','x']])

    def test_check6(self):
      arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      ans = ex6(arr)
      self.assertEqual(ans, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_check7(self):
      arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      ans = ex7(arr)
      self.assertEqual(ans, [[1, 2, 3], [4, 5, 6]])

    def test_check8(self):
      arr = [[1,2,3]]
      ans = ex8(arr, [1,1,1])
      self.assertEqual(ans, [[1,2,3],[1,1,1]])

if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()