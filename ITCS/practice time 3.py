householdObjs = ['chair', 'desk', 'bed', 'TV', 'sofa']

for obj in householdObjs:
    print(obj)

print("")

householdObjs[2] = 'dining table'

for obj in householdObjs:
    print(obj)

print("")

del householdObjs[1]

for obj in householdObjs:
    print(obj)

print("")

householdObjs.insert(3, 'dvd player')

for obj in householdObjs:
    print(obj)

print("")
