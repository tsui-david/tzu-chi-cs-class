"""
SLICING REVIEW
- For ex1-4 use the slicing operator only
- That means do something like s[1:2], s[1:], s[:1], etc

Good resource:
https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
"""

def ex1(s):
    """
    Given a string s, return string that goes up to the first 3 characters
    EX:
    "abcdefg" --> "abc"
    """

def ex2(s):
    """
    Given a string s, return string that takes the 3rd character and onward
    EX:
    "abcdefg" --> "cdefg"
    """

def ex3(s):
    """
    Clone a copy of the string
    Hint: You can slice this.... from beginning to end!
    EX:
    "abcdefg" --> "abcdefg"
    """

def ex4(s):
    """
    Practice using negative index access:
    EX:
    s[-1] returns the last character

    Retrieve a string up to the last 3 characters of the string

    "abcdefg" --> "abcd"
    """

"""
STRING IMMUTABILITY
- Strings are immutable. This means that whennever you are manipulating strings (such as slicing) you are creating a BRAND NEW new string.
- ex: a = "abc", a[:-1], a is still "abc"
- On the other hand, an array can be changed. It is MUTABLE. ex: a = [1] a.append(2). a is now [1,2]!

"""

def ex5(s1, s2):
    """
    Return True if s1 and s2 are the same in value

    ex: s1 = "abcde", s2 = "abcde"

    return True

    You are NOT allowed to use s1 == s2

    Use for loop instead!
    """

"""
STRINGS to ARRAY to STRINGS

Strings can be converted into array for easy manipulation (pop, append, etc)

To convert a string to an array use the list() operator:
s = "abc"
b = list(s) --> ['a', 'b', 'c']

To convert an array to a string use the join operator:
c = ''.join(b) --> "abc"

RESOURCE: 
https://www.geeksforgeeks.org/join-function-python/
"""
def ex6(s1, s2):
    """
    PROBLEM:
    Given a string s1 and s2, merge the two strings character by character, starting with s1 as first character

    EXAMPLE:
    s1 = "abc", s2 = "def"
    return "adbecf"
    """
    
    merge = []

    i = 0
    j = 0

    merge_s1 = True
    while i < len(s1) and j < len(s2):
        if merge_s1:
            merge.append(s1[i])
            i += 1
            merge_s1 = False
        else:
            merge.append(s2[j])
            j += 1
            merge_s1 = True
    
    while i < len(s1):
        merge.append(s1[i])
        i += 1
    
    while j < len(s2):
        merge.append(s2[j])
        j += 1
    
    return "".join(merge)


