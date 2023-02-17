class Zoo:
    def __init__(self, zoo_name):
        self.animal = list()
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animal:
            self.animal.append(new_animal)

    def get_animals(self):
        print(self.animal)

    def sell_animal(self, animal_sold):
        if animal_sold not in self.animal:
            print('Sorry the animal is not in the list')
        else:
            self.animal.remove(animal_sold)

    def sort_animals(self):
        sort = {}
        for animal in self.animal:
            if animal[0] not in sort:
                sort[animal[0]] = [animal]
            else: 
                sort[animal[0]].append(animal)
        sort = dict(sorted(sort.items()))
        return sort

    def get_groups(self):
        sort = self.sort_animal()
        for key, value in sort.items():
            print(f'{key}  {value}')


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal('Giraffe')
