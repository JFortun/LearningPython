import math

def sum(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("You can't divide by 0")
        return "Error"


while True:
    try:
        number1 = (int(input("Set the first number: ")))
        number2 = (int(input("Set the second number: ")))
        break
    except ValueError:
        print("Introduce only numbers")

operation = input("Select the wanted operation (sum, subtraction, multiplication or division): ")

if operation == "sum":
    print(sum(number1, number2))
elif operation == "subtraction":
    print(subtraction(number1, number2))
elif operation == "multiplication":
    print(multiplication(number1, number2))
elif operation == "division":
    print(division(number1, number2))
else:
    print("Operation not valid")


def division2():
    try:
        number1 = (float(input("Set the first number: ")))
        number2 = (float(input("Set the second number: ")))
        print("The result is: " + str(number1 / number2))
    except ValueError:
        print("Introduce only numbers")
    except ZeroDivisionError:
        print("You can't divide by 0")
    finally:
        print("Finished")

division2()

def evalueAge(age):
    if age < 0 or age > 100:
        raise ValueError("Invalid age")

    if age < 20:
        return "You are very young"
    elif age < 40:
        return "You are young"
    elif age < 60:
        return "You are mature"
    elif age < 100:
        return "You are old"
    
print(evalueAge(101))

def calculateRoot(number1):
    if number1 < 0:
        raise ValueError("The number can't be negative")
    else:
        return math.sqrt(number1)

try:
    print(calculateRoot(-144))
except ValueError as NegativeNumber:
    print(NegativeNumber)

print("finished")