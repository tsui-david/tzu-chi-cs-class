## Class Notes

### Review
Last class we reviewed the following concepts:
- [x] If/else statements
- [x] getting user input
- [x] the use of "modulo" --> %

### Functions
As a review the syntax for functions is:
```
def function_name(parameter):
    # write function logic here
    # (optional) return something

param = 1
# call the defined function
function_name(param)
```
- A function is created through `def name():` as the basic syntax
- Anything you pass inside the parenthesis are **arguments** that allows you to pass in dynamic values
- Note how `param` is **passed** into the parenthesis and is realized as the value
of 1. In the function `function_name` parameter thus now equals 1.
- A function can `return` something. If you do not type `return` python by default `return None`

Example:
```
print(function_name(param)) # this will print out None
```
Example 2:
```
def function_name(parameter):
    return parameter+1

print(function_name(1)) # this will print out 2
```

- Variables created inside functions cannot be accessed outside of the function except through `return`
- This concept is known as **scope**, where variables are hidden away and cannot be accessed depending on where it is.
Example 3:
```
def blah():
    my_cool_variable = 1

print(my_cool_variable) # this will result in error!
```

- In contrast however, variables defined prior to the function and in the main program file can be accessed
Example 4:
```
my_cool_variable = 1
def blah(param):
    return param + my_cool_variable
print(blah(1)) # prints 2
```
- Ultimately the point of using functions is to organize and reuse your code so you don't have to do something over and over again.

```
def add(a, b):
    return a + b

print(add(1, 2))
print(add(2, 3))
print(add(3, 4))
```


### Loops
Loops are another way to repeat something over and over again in Python.

One way for looping is **for loop**

Syntax:
```
# print 0, 1, 2, ... 8
for variable in range(9):
    print(variable)
```
- `range(num)` is a function that gives you a `list` of numbers from 0 to num - 1
- Don't worry, we will get to more about `list` later on
- In this function, the `variable` will represent elements from the list one at a time
- `range()` can also accept 2 **arguments** instead of 1

Example 1:
```
for variable in range(2, 9):
    print(variable)
# this prints out 2, 3, 4, ... 8
```

Another form of looping which might give you greater control is a **while loop**

Syntax:
```
# print 0, 1, 2, ... 8
variable = 0
conditional = variable < 9 
while conditional:
    print(variable)
    variable += 1
```

Be careful of while loops as it is easy to create an **infinite loop**
Example 2:
```
while True:
    print("HI")

# keeps print "HI" until your computer realizes something is wrong and shuts the program down
```

- A while loop needs a conditional to keep looping.
- While the conditional is true, the code within the while loop will execute

Another way to exit loop is simply by using `break`
Example 2:
```
While True:
    print("HI")
    break
# prints "HI" once and then breaks and exits
```

Example 3:
```
for i in range(9):
    print(i)
    break
# prints 0 and exits
```