tuple = ("Joan", 12, 15.6, 15.6, True)

print(tuple[2])

list = list(tuple) #Convert a tuple to a list

print(list)
print("Joan" in tuple)
print(tuple.count(15.6))
print(len(tuple))

unitaryTuple = ("One",) #Important the "," in unitary tuples

timeTuple = ("Joseph", 11, "January", 2020)

name, day, month, year = timeTuple

print(name, day, month, year)