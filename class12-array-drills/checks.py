import unittest
from drills import *

class CheckDrills(unittest.TestCase):
    def test_example(self):
        ans = example()
        self.assertEqual(ans, 'wow!')
  
    def test_ex1(self):
        ans = ex1([1,2,3,4,5])
        self.assertEqual(ans, 5)
    
    def test_ex2(self):
        ans = ex2([1,2,3])
        self.assertEqual(ans, 1)
    
    def test_ex3(self):
        ans = ex3([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(ans, 10)
    
    def test_ex4(self):
        ans = ex4()
        self.assertEqual(ans, ['a','a','a','a','a'])
    
    def test_ex5(self):
        ans = ex5()
        compare = ['a'*100]
        self.assertEqual(ans, compare)
    
    def test_ex6(self):
        ans = ex6(6)
        self.assertEqual(ans, ['a','a','a','a','a','a'])
    
    def test_ex7(self):
        ans = ex7([1,2,3])
        self.assertEqual(ans, [1,2])

    def test_ex8(self):
        ans = ex7([1,2,3])
        self.assertEqual(ans, [1])

    def test_ex9(self):
        ans = ex7([1,2,3],3)
        self.assertEqual(ans, [1])

    def test_ex10(self):
        test = [1,2,3]
        ans = ex10(test)
        self.assertIsNot(test, ans)
        self.assertEqual(ans, [1,2,3])

    def test_ex11(self):
        test = [1,2,3]
        ans = ex11(test)
        self.assertEqual(ans, [1,2,3,1,2,3,1,2,3])  

    def test_ex12(self):
        self.assertEqual(ex12(5), [[],[],[],[],[]])

    def test_ex13(self):
        a = [[0],[1]]
        self.assertEqual(ex13(a), 0)
    
    def test_ex14(self):
        a = [[0],[1]]
        self.assertEqual(ex14(a), 1)
    
    def test_ex15(self):
        a = [[0],[1]]
        self.assertEqual(ex15(a, 0, 0), 0)

if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()