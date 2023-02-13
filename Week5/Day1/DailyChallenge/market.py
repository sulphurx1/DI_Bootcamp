class Farm():
    def __init__(self, name):
        self.name = name
        print(f'{self.name}'+ 's farm')

    def add_animal(self, type, amount):
        self.type = type
        self.amount = amount
        print(f'{self.type} : {self.amount}')

    def get_info(self):
        print(f'E-I-E-I-0!')

        



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())