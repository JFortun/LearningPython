print("Write your grade in the exam")
grade = input()


def evaluation(grade):
    rating = ""
    if 0 < grade < 5:
        rating = "Failed"
    elif grade > 10:
        rating = "Incorrect grade (more than 10)"
    elif grade < 0:
        rating = "Incorrect grade (less than 0)"
    else:
        rating = "Approved"
    return rating


print("Your evaluation is: " + evaluation(int(grade)))  # int() to convert sring to int

print("Student grants 2020")

distance_school = int(input("Set the distance between the school and your home in km "))
print(distance_school)
number_brpthers = int(input("How many brothers do you have? "))
print(number_brpthers)
family_income = int(input("set your family's annual income "))
print(family_income)

if distance_school > 50 and number_brpthers > 4 or family_income <= 2000:
    print("You have the right to receive a grant")
else:
    print("You don't have the right to receive a grant")

print("Optative subjects")
print("Subjects: Coding1, Coding2, Coding3")
subject = input("Select your desired subject ")
if subject in ("Coding1", "Coding2", "Coding3"):
    print("Subject " + subject + " selected")
else:
    print("Subject not valid")
