"""
Last week we created a program that accepts user input for number
and checks for: 
(1) If number is odd, print out "odd"
(2) If number is even, print out "even"
"""
input_num = int(input('Input a number: '))
if input_num % 2 == 0:
    print("even")
else:
    print("odd")


"""
This week I want you to keep asking the user for numbers and print out even/odd until the user types in "stop"
Todo this I would like the following requirements:
- [ ] Until the user types in "stop" do not exit the code (hint: what allows us to do things over and over again?)
- [ ] Organize the even/odd logic into a function called "getEvenOdd"
- [ ] getEvenOdd will return the string "even" if the argument is even and "odd" if the argument is "odd"
- [ ] use getEvenOdd in your program
"""

