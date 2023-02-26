magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

def make_great(magician_names):
    great_magicians = list()
    while magician_names:
        magician = magician_names.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magician_names.append(great_magician)


make_great(magician_names)
show_magicians(magician_names)