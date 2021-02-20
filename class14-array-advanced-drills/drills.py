def ex1(a):
  """
  given an array of integers, find and return the smallest integer's INDEX

  ex: a = [1,2,3,4]
  return 0
  """

def ex2(a, target):
  """
  given an array of UNIQUE words, find and return the matching INDEX in the array.
  if no such word, return -1
  
  ex: a = ["such", "cool"], target = "cool"
      return 1

  ex: a = ["such", "cool"], target = "nope"
      return -1
  """

def ex3(a, target):
  """
  given an array with DUPLICATE words, find and return ALL matching indices in the array.
  if no such word, return empty array

  answer can be in ANY ORDER

  ex: a = ["wow", "such", "such", "cool"] target = "such"
      return [1,2]

  ex: a = ["wow", "such", "such", "cool"] target = "nope"
      return []
  """

# this will be hard, keep going!
def ex4(a, target):
  """
  given an array of integers, find first PAIRS(2) of numbers which sum to target
  return as a tuple
  
  if no pair return None

  ex: a = [1,2,3,4] target = 3
  return (1,2) # Notice how we can't return 3 because 3 is not a pair
  """

# same same but different, still hard though!
def ex5(a, target):
  """
  given an array of integers, find PAIRS of numbers which sum to target
  return all possible solutions as an array of tuple pairs
  if no pairs return empty array
  
  answer can be in ANY ORDER

  ex: a = [1,2,3,4] target = 5
  return [(1,4), (2,3)]

  hint: to create a tuple, simply use paranthesis around 2 or more values:
  (3,4) or (a[1], a[2]), etc

  Q: Why do we use tuple vs array though? They seem to achieve the same purpose right?
  A: Sort of. They both store list of numbers. However tuples are immutable, ie they can't be changed vs arrays can be changed (via append or pop).
  This allows tuples to be sorted which is what we're doing to check whether the answer can be in any order or not
  
  ^^ You don't need to really know that stuff for the purpose of this question. But it's just something to keep in mind in case you're curious.
  """

# not so bad now right?
def ex6(a, target):
  """
  given an array of integers, find PAIRS OR SINGLE number which sum to target
  return all possible solutions as an array of tuple or single
  if no match return empty array

  answer can be in ANY ORDER
  
  ex: a = [1,2,3,4] target = 3
  return [(1,2), (3)] <--- NOTICE HOW 3 IS ALSO STORED AS TUPLE

  hint: to convert single integer to tuple, we can do something like
  tuple([3]) to convert 3 --> (3)
  https://stackoverflow.com/questions/35857209/converting-integer-of-tuple-to-string-of-tuple
  """

# yaaaaa 
def ex7(a):
  """
  given an array, return True if all values in array is the same 

  ex: a = ["X", "X", "X"]
  return True
  """

# it's rewind time!!!
def ex8(a):
  """
  given an array, return True if any row/column in the array is the same

  ex: a = [
            ["X", "O", "X"],
            ["X", "O", "X"],
            ["O", "O", "+"],
          ]
  return True because COL 1 is all same

  hint: reuse ex7 function for finding rows

  Q: what about finding same cols?
  A: try traversing row by row for every col rather than the classic col by col for every row

  good luck!!
  """





## No more array drills now :) Congrats!       ##
## We will start something brand new next week ##