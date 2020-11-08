# Create a calculator app!

#The app will accept user inputs first with the options of: "add", "multiply", "subtract", "divide".

#Then the app will accept two values, one after another.

#After the user has entered the two values, you should return the correct answer.

#Make use of functions for each operation - you should have 4 functions in total.

#Keep asking the user until the user types in "stop".

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def check_stop(inputString):
    return inputString == "stop"
        
def manage_input():
    operation = input("Please enter operation: [ +,-,*,/ ]: ")
    if check_stop(operation):
        return False, None, None, None
    
    num1 = input("Please enter first number: ")

    if check_stop(num1):
        return False, None, None, None

    num2 = input("Please enter second number: ")

    if check_stop(num2):
        return False, None, None, None

    return True, operation, float(num1), float(num2)


can_continue, operation, n1, n2 = manage_input()
while can_continue:
    print(operation)
    if operation == "+":
        print(add(n1, n2))
    elif operation == "-":
        print(subtract(n1, n2))
    elif operation == "*":
        print(multiply(n1, n2))
    elif operation == "/":
        print(divide(n1, n2))
    else:
        print("error! no operation found")
    
    can_continue, operation, n1, n2 = manage_input()
