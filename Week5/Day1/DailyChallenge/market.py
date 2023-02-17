class Farm():
    def __init__(self, name):
        self.name = name
        self.animal ={}

    def add_animal(self, type):
        count = 1
        if type in self.animal:
            self.animal[type] += count
        else:
            self.animal[type] = count

    def get_info(self):
        print(f'E-I-E-I-0!')

        



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())