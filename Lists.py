list = [2, "Dog", 3.5, "Cat", 35, 12, False]
list2 = [True, 34, 67.5, "Snake"]
list3 = [1,2,3] * 10

print(list[2])
print(list[0:3])
print(list[2:])

list.append(18.5) #Inserts at the end
list.insert(5, "bird") #Inserts ant given index
list.extend(["Whale", "Ape"]) #Insert some elements at the end of the list

print(list) #Prints the full list
print(list.index("Cat")) #Print the position (index) of "Cat"

print("Dog" in list)
print("Human" in list)

list.remove(12) #Removes a given element
list.pop() #Removesn the last element introduced

print(list)

listSum = list + list2

print(listSum[:])
print(list3)