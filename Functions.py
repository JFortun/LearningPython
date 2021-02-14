def lines():
    print("Line1")
    print("Line2")
    print("Line3")


def sum():
    a = 14
    b = 21
    print(a + b)


def subtraction(num1, num2):
    print(num1 - num2)


def division(num1, num2):
    result = num1 / num2
    return result


lines()
sum()
subtraction(126, 56)
print(division(45, 12))

store_result = division(55, 5)
print("The result is: " + str(store_result))
