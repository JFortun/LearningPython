import math

for i in [1, 2, 3, 4, 5]:
    print("Number " + str(i))

for i in ["One", "Two", "Three", "Four", "Five"]:
    print("Number " + i)

for i in [1.0, 2.0, 3.0, 4.0, 5.0]:
    print("Number " + str(i))

for i in range(3):
    print("Hi")

for i in range(3):
    print(f"Value {i}")

for i in range(5, 10): #From 5 to 10
    print(f"Value {i}")

for i in range(5, 10, 2): #From 5 to 10 and in pairs
    print(f"Value {i}")

counter = 0
email = input("Inset your email address ")

for i in email:
    
    if (i == "@" or i == "."):
        counter = counter + 1

if counter >= 2:
    print("Its a mail")
else:
    print("Is not a mail")

i = 1
while i <= 10:
    print("Execution " + str(i))
    i = i + 1
print("Finished")

print("-----Square root calculator-----")
number = int(input("Enter a number to find its square root"))
attemps = 0
while number < 0:
    print("negative numbers do not have a square root")
    if attemps == 3:
        print("Too much attemps. Program is finished")
        break
    number = int(input("Enter a number to find its square root"))
    if number < 0:
        attemps = attemps + 1
if attemps < 3:
    solution = math.sqrt(number)
    print("The square root of " + str(number) + " is " + str(solution))

for letter in "Python":
    if letter == "h":
        continue
    print("Currently at letter" + letter)

name = "Anthony Jones"
print(str(len(name)) + " characters with spaces")
counter = 0

for i in name:
    if i == " ":
        continue
    counter = counter + 1

print(str(counter) + " characters without spaces")

class MyClass:
    pass # Sets null value

