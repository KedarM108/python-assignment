'''Calculator using if-else and functions
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Factorial of a given number
It takes the input from the user.
It also displays Menu of the operation that the user is allowed to perform.'''


def add(x, y):
    z = x + y
    return z


def sub(x, y):
    z = x - y
    return z


def multi(x, y):
    z = x * y
    return z


def div(x, y):
    z = x / y
    return z


def fact(x):
    if x < 0:
        print("Factorial for negative number doesn't exist")
    elif x == 0:
        print("Factorial of 0 is 1")
    else:
        f = 1
        for i in range(1, x + 1):
            f = f * i
        print(f)


while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        number1 = int(input("Enter the first number:"))
        number2 = int(input("Enter the second number:"))
        print(add(number1, number2))
    elif choice == 2:
        number1 = int(input("Enter the first number:"))
        number2 = int(input("Enter the second number:"))
        print(sub(number1, number2))
    elif choice == 3:
        number1 = int(input("Enter the first number:"))
        number2 = int(input("Enter the second number:"))
        print(multi(number1, number2))
    elif choice == 4:
        number1 = int(input("Enter the first number:"))
        number2 = int(input("Enter the second number:"))
        print(div(number1, number2))
    elif choice == 5:
        number1 = int(input("Enter the number:"))
        print(fact(number1))

    else:
        print("invalid choice")
        break
