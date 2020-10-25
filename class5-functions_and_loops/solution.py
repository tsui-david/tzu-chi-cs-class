def getEvenOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

while True:
    user_input = input("Enter your number: ")
    if user_input == "stop":
        break
    
    print(getEvenOdd(int(user_input)))