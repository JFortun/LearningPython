dictionary = {"One":1, "Two":2, "Three":3}
print(dictionary["Two"])

dictionary["Four"] = 5 #Add a new element
print(dictionary)

dictionary["Four"] = 4 #Modify an element
print(dictionary)

del dictionary["Two"] #Delete an element
print(dictionary)

tuple = ("a", "e", "i", "o", "u")
dictionaryTuple = {tuple[0]:"Ha", tuple[1]:"He", tuple[2]:"Hi", tuple[3]:"Ho", tuple[4]:"Hu"} #Inseting a tuple inside a dictionary
print(dictionaryTuple["o"])