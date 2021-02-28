def ex1():
    """
    - We have seen strings before. Strings can be instantiated with single quote '' or double quote ""
    
    PROBLEM: Try to create a variable with a string value, 'hello' and return it.
    """

def ex2(a):
    """
    - Strings can be concactenated (joined together)
    - You can add to strings together by using the + operator on two strings.
    
    PROBLEM: Given an array of strings, return one string that concactenates all the elements in the array.
    INCLUDE a space in between each string.

    example:
    a = ["hello", "world"]

    return "hello world"
    """

def ex3(s):
    """
    - Strings are similar to arrays! To be more specific, they are an array of characters! 
    - Each index in the string will represent a character
    
    PROBLEM: Given a string, return the first AND last character of the string
    - hint: you can return multiple elements using the comma

    EXAMPLE:
    "hello"
    return "h", "o"
    """

def ex4(s, i, j):
    """
    - You might've used the "slice" operation in python to truncate arrays.
    - example: 
    a = [4,5,6,7]

    You can "slice" the array of a from the 1st element onward:
    a[1:] --> [5,6,7]

    Or you can "slice" the array from the 1st element backward:
    a[:1] --> [4]

    Or you can "slice" the array from the 1st (inclusive) to the 3rd element (not inclusive):
    a[1:3] --> [5,6]

    - Similarly, you can do the same thing with strings!!

    What would a[1:1] give?

    - answer: []
    - why? Because we go from 1 to 1 (not inclusive) so it's empty!



    PROBLEM: Given a string return a slice of the string from i (inclusive) to j (not inclusive)

    example:
    s = "abc", i = 1, j = 2
    return "b"
    """

def ex5(s1, s2):
    """
    Problem: Given s1 and s2, return True if s1 contains s2. return False if s1 does not contain s2

    example:
    s1 = "TreasureIsland" s2 = "Island" --> True
    s1 = "TreasureIsland" s2 = "X!!@" --> False

    You can assume s2 will be smaller to or equal to s1  
    """

def ex6(s1):
    """
    While string is similar to an array, it is NOT an array. Strings are immutable. This means once a string is created, it cannot be changed.
    When we concatenate two strings, we are simply creating a brand new string. So ex2 problem is actually pretty inefficient if we are using the + operator.

    On the other hand, an array can be changed. It is MUTABLE. ex: a = [1] a.append(2). a is now [1,2]!

    Sometimes it is handy to add characters to an array and then join it back because strings can't be "appended".

    To do this we can do:

    a = []
    a.append("a")
    a.append("b")
    a.append("c")

    a_str = "".join(a) --> "abc"

                ^ the join combines the array element by element with the "" in between.

    if we do:

    a_str = "*".join(a) --> "a*b*c"  
    
    PROBLEM:
    Given a string s1, add a "*" in between each character

    Example:
    s1 = "abc"
    return "a*b*c"
    """

def ex7(s1, s2):
    """
    PROBLEM:
    Given a string s1 and s2, merge the two strings character by character, starting with s1 as first character

    EXAMPLE:
    s1 = "abc", s2 = "def"
    return "adbecf"
    """