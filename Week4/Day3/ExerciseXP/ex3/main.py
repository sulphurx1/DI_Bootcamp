# Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
brand = {
    'name': 'Zara',
    'creation_date': '1975',
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': '7000',
    'major_color':{'France': 'blue', 'Span': 'red', 'US': ['pink', 'green']} 
}

# Change the number of stores to 2.
brand['number_stores'] = 2

# Print a sentence that explains who Zaras clients are.
print(brand['name'] + ' was created in ' + brand['creation_date'] + ' by ' + brand['creator_name'])

# Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'Spain'

# Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

# Delete the information about the date of creation.
brand['creation_date'] = ''

#Print the last international competitor.
print(brand['international_competitors'][-1])

# Print the major clothes colors in the US.
x = brand['major_color'].get('US')
print(', '.join(x))

# Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

# Print the keys of the dictionary.
the_key_list = list()
for key in brand.keys():
    the_key_list.append(key)

print(', '.join(the_key_list))

# Create another dictionary called more_on_zara with the following details
more_on_zara = {
    'creation_date': 1975,
    'number_stores': '10 000'
}

brand.update(more_on_zara)

# Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])
''' the initial value of '2' was overwrite with '10 000' '''