class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

all_cats  = [Bengal('whiskers', 8), Chartreux('felix', 4), Siamese('oscar', 6)]

sara_pet = Pets(all_cats)
sara_pet.walk()
    