phones = ['galaxy s2', 'realme x50 5g', 'galaxy s7', 'galaxy s10e', 'xperia z2',
          'samsung s24 ultra', 'iphone 7', 'iphone x', 'lg optimus one']

#printing with a slice index of 2:5 means that we'll print items 2, 3, and 4. 
print(phones[2:5])

#putting a colon in between square brackets means that we're using slicing.
#placing only a number after the colon and not before,
#means that the first number will be zero

print("")

print(phones[:4])

for phone in phones[3:6]:
    print(phone.title())

#We can add a third number to the square brackets:
#this will cause the list to skip by the incremented amount.

print("")

for phone in phones [:9:2]:
    print(phone.title())



