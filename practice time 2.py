intA, intB, intC = 10,20,30

intD, stringA, floatA, stringB = 33, "car", 2.158, "hey"

print(str(intD) + stringA + str(floatA) + stringB)

namesAndAges = {"Dave": '41', "Bob": '22', "Mark": '38'}

for key, value in namesAndAges.items():
    print(F"The person {key} is of age {value}.")

gameNames = ['Left 4 Dead 2', 'Back 4 Blood', 'Balatro', 'Animal Crossing']

#In the above list, L4D2 has index number 0, Balatro has index number 2.

#We can also access the indices using negative numbers,
#if we want to search from the end of the list
#without knowing the positive index number of the very last item.

#When using negative indices, Animal Crossing has an index of -1.

print(gameNames[-1])

print(gameNames[-3] + ", " + str(type(gameNames[-3])))

