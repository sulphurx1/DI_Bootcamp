cost = 0
ages = list()


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

for keys, values in family.items():
    if values < 3:
        cost = 0
    elif values >= 3 and values <= 12:
        cost = 10
    else:
        cost = 15
    print(f'{keys} has to pay: ${cost}')

for value in family.values():
    ages.append(value)


for age in ages:
    if age < 3:
        cost += 0
    elif age >= 3 and age <= 12:
        cost += 10
    else:
        cost += 15

print(f'The total cost family has to pay: ${cost}')