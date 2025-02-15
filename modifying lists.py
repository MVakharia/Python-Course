colours = ['red', 'blue', 'green', 'yellow']

print(colours)

#You can append an item to a list using the '+' operator. 

colours = colours + ['orange']

print(colours)

#You can change an item in a list by getting the list name
#and index number and entering a new value. 

colours[1] = 'black'

print(colours)

#You can insert an item into the middle of a list by getting an index number:
#the item will be placed behind that value, with an index number of one less
#than the value it's going behind.

colours.insert(2, 'white')

print(colours)

del colours[3]

print(colours)

colours.remove('yellow')

print(colours)
