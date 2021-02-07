"""
- The following are a list of exercises to get you familiar with loops, arrays, and variables.
- After you complete the exercsise, run the checks.py file to see if you passed the basic checks.
- test
"""

def example():
  return 'wow!'

def ex1(a):
    """
    given an array return the 5th element in the array
    """
    return a[4]

def ex2(a):
    """
    given an array return the first element in the array
    """
    return a[0]

def ex3(a):
    """
    given an array return the last element in the array
    """
    return a[-1]

def ex4():
    """
    create an array with 5 character "a" inside
    """
    a = []
    for i in range(5):
        a.append('a')
    return a

def ex5():
    """
    create an array with 100 character "a" inside
    """
    a = []
    for i in range(100):
        a.append('a')
    return a

def ex6(n):
    """
    given an input n, create an array with n character "a" inside
    """
    a = []
    for i in range(n):
        a.append('a')
    return a

def ex7(a):
    """
    given an array, remove the last element
    if array is empty return empty
    """
    if len(a) == 0:
        return []
    a.pop()
    return a

def ex8(a):
    """
    given an array, remove all BUT the first element
    if array is empty return empty
    [1,2,3] -> [1]
    """
    if len(a) == 0:
        return []
    
    while len(a) > 1:
        a.pop()
    return a

def ex9(a,n):
    """
    given an array, and n, remove n elements from the array
    if array is empty return empty
    """
    if len(a) < n:
        return []
    
    for i in range(n):
        a.pop()
    return a

def ex10(a):
    """
    given an array, return a new array that is a copy of the array
    """
    return a[:]

def ex11(a):
    """
    given an array, return an array that copies the input array 3 times.
    ex: [1] -> [1,1,1]
        [2,2] -> [2,2,2,2,2,2]
    """
    b = []
    for i in range(3):
        for j in range(len(a)):
            b.append(a[j])
    return b

def ex12(n):
    """
    create an array of n arrays
    """
    a = []
    for i in range(n):
        a.append([])
    return a

def ex13(a):
    """
    given a 2d array, return the first element of the first array
    """
    return a[0][0]

def ex14(a):
    """
    given a 2d array, return the last element of the last array
    """
    return a[-1][-1]

def ex15(a, i, j):
    """
    given a 2d array return the jth element of the ith array
    """
    return a[i][j]