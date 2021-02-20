def ex1(a):
  """
  given an array of integers, find and return the smallest integer's INDEX

  ex: a = [1,2,3,4]
  return 0
  """
  min_num = float('inf')
  min_index = -1
  for i, v in enumerate(a):
    if v < min_num:
      min_index = i
      min_num = v
  
  return min_index

def ex2(a, target):
  """
  given an array of UNIQUE words, find and return the matching INDEX in the array.
  if no such word, return -1
  
  ex: a = ["such", "cool"], target = "cool"
      return 1

  ex: a = ["such", "cool"], target = "nope"
      return -1
  """
  for i in range(len(a)):
    word = a[i]
    if word == target:
      return i
  
  return -1


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
  ans = []
  for i in range(len(a)):
    word = a[i]
    if word == target:
      ans.append(i)
  
  return ans

# this will be hard, keep going!
def ex4(a, target):
  """
  given an array of integers, find first PAIRS(2) of numbers which sum to target
  return as a tuple
  
  if no pair return None

  ex: a = [1,2,3,4] target = 3
  return (1,2) # Notice how we can't return 3 because 3 is not a pair
  """
  for i in range(len(a)):
    for j in range(i, len(a)):
      if a[i] + a[j] == target:
        return (a[i], a[j])

  return None


# same same but different, still hard though!
def ex5(a, target):
  """
  given an array of integers, find PAIRS of numbers which sum to target
  return all possible solutions as an array of tuple pairs
  if no pairs return empty array
  
  answer can be in ANY ORDER

  ex: a = [1,2,3,4] target = 5
  return [(1,4), (2,3)]
  """
  ans = []
  for i in range(len(a)):
    for j in range(i, len(a)):
      if a[i] + a[j] == target:
        ans.append((a[i],a[j]))
  return ans

# same same but different again!
def ex6(a, target):
  """
  given an array of integers, find PAIRS OR SINGLE number which sum to target
  return all possible solutions as an array of tuples
  if no match return empty array

  answer can be in ANY ORDER
  
  ex: a = [1,2,3,4] target = 3
  return [(1,2), (3)] <--- NOTICE HOW 3 IS ALSO STORED AS TUPLE
  """
  ans = []
  for i in range(len(a)):
    if a[i] == target:
      ans.append(tuple([a[i]]))
    for j in range(i, len(a)):
      if a[i] + a[j] == target:
        ans.append((a[i],a[j]))

  return ans


# yaaaaa 
def ex7(a):
  """
  given an array, return True if all values in array is the same 

  ex: a = ["X", "X", "X"]
  return True
  """
  for i in range(1, len(a)):
    if a[i] != a[i-1]:
      return False
  
  return True

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
  """
  
  M = len(a)
  N = len(a[0])
  # check rows
  for i in range(len(a)):
    if ex7(a[i]):
      return True
  # check cols
  # we're going to loop by columns first for i, and loop by rows for j
  # this allows us to traverse row by row for each column instead of the classic column by column for each row
  for i in range(N):
    current_col_is_same = True
    for j in range(1, M):
      if a[j][i] != a[j-1][i]:
        current_col_is_same = False
        break

    if current_col_is_same:
      return True
    

  return False



## No more array drills now :) Congrats!       ##
## We will start something brand new next week ##