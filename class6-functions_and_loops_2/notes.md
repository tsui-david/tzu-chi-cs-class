## Class Notes

### Review
Last class we went over:
- [x] function definition
- [x] applying functions
- [x] while loop
- [x] for loop

### Solution Review
If you recall, our problem we were working on was:

```
This week I want you to keep asking the user for numbers and print out even/odd until the user types in "stop"
Todo this I would like the following requirements:
- [ ] Until the user types in "stop" do not exit the code (hint: what allows us to do things over and over again?)
- [ ] Organize the even/odd logic into a function called "getEvenOdd"
- [ ] getEvenOdd will return the string "even" if the argument is even and "odd" if the argument is "odd"
- [ ] use getEvenOdd in your program
```

In order to solve this problem, we need to create a function for the even/odd logic.

```
def getEvenOdd(param):
    if param % 2 == 0:
        return "even"
    else:
        return "odd"
```

To properly define the function, we should add a dynamic parameter. For the example above we call it `param`.
We use modulo to determine if it is even or odd.

Now that we have defined the `getEvenOdd(param)` we can use it in our `main` application by simply invoking the function itself.

```
def getEvenOdd(param):
    if param % 2 == 0:
        return "even"
    else:
        return "odd"

getEvenOdd(1) # <--- function invoked with param = 1
```

Although we do not see anything because we didn't print, `getEvenOdd(1)` would be returning "odd".

Again the `return` keyword allows for values from the function to be visible in the `main` application. Check back to previous lesson on `scope` for review.

Great! So we took care of the `getEvenOdd` part. Let's try to tackle the other parts.

If you remember from previous classes, we can ask for user input with `val = input('Please enter your number: ')`

So our program will look like:
```
def getEvenOdd(param):
    if param % 2 == 0:
        return "even"
    else:
        return "odd"

val = input('Please enter your number: ')
print(getEvenOdd(int(val)))
```

val is a string that is returned from `input()` which is the function that asks the user for inputs.
`getEvenOdd()` accepts integers and not string however so we need to convert it to integers. We can do this by `casting` the value to int with `int(val)`.

We have now a working program where the program asks the user for input and tells you whether it is even or odd.

How do we continuously ask the user?

We can use a `while loop`:

```
def getEvenOdd(param):
    if param % 2 == 0:
        return "even"
    else:
        return "odd"

while True:
    val = input('Please enter your number: ')
    print(getEvenOdd(int(val)))
```

This will be an infinite loop that will loop forever.

In order to stop, we need to `break` out of the loop OR make the `True` condition `False`.

This can be done with:

```
while True:
    val = input('Please enter your number: ')
    if val == "stop":
        break
    print(getEvenOdd(int(val)))
```

or

```
val = "" # some initial value that is not stop

while val != "stop":
    val = input('Please enter your number: ')
    if val.isnumeric():
        print(getEvenOdd(int(val)))
```

Notice how if I try to `int(val)` when val is not an int, the program will freak out. However `val.isnumeric()` will let me know if it is a number before I force cast the val variable.


### Problem of the Week!

Create a calculator app!
1. The app will accept user inputs first with the options of: "add", "multiply", "subtract", "divide".
2. Then the app will accept two values, one after another.
3. After the user has entered the two values, you should return the correct answer.
4. Make use of functions for each operation - you should have 4 functions in total.
5. Keep asking the user until the user types in "stop".

Hint:
```
Operations in python are: +, -, *, /

ex:
1 + 1
1 - 1
1 * 1 
1 / 1
```

Challenge 1: Do NOT use the `*` operator for multiply

Challenge 2: Create an additional option: `square` which only accepts **ONE** input value instead of two and prints the squared value.

Example Output:
```
Operations in python are: +, -, *, /: +
what is your first number:1
what is your second number:2
3

Operations in python are: +, -, *, /:*
what is your first
```