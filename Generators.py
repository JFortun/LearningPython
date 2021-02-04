#way to do it with a function
def generatesPairsFunction(limit):
    number = 1
    list = []
    while number < limit:
        list.append(number*2)
        number = number + 1
    return list

print(generatesPairsFunction(10))

#way to do it with a generator
def generatesPairsGenerator(limit):
    number = 1
    while number < limit:
        yield number*2
        number = number + 1

returnsPairs = generatesPairsGenerator(10) #To see the result
#for i in returnsPairs:
#    print(i)

print(next(returnsPairs)) #Use next to get values one at one from the generator
print("new code lines here")
print(next(returnsPairs))
print("new code lines here")
print(next(returnsPairs))
print("new code lines here")

def generatesCities(*cities): #* to indicate that its going to receive an indeterminated number of items in form of a tuple
    for element in cities:
        #for subElement in element: #Unnecessary with yield from
            #yield from subElement  #Unnecessary with yield from
        yield from element

returnCities = generatesCities("Madrid", "Barcelona", "Seville", "Valencia")
print(next(returnCities))
print(next(returnCities))