employees = ['Tom', 'Richard', 'Harry', 'Becca', 'Amy']

for employee in employees:
    print(employee)

name = 'harry'

nameToTitle = name.title()

if nameToTitle in employees:
    print(nameToTitle + ' works here.')
else:
    print(nameToTitle + ' does not work here.')

print(len(employees))
