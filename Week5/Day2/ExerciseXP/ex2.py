class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        the_speed = self.weight / (self.age * 10)
        return the_speed
    
    def fight(self, other_dog):
        self.other_dog = other_dog
        if ((self.run_speed() * (self.weight)) > (other_dog.run_speed() * (other_dog.weight))):
            print(f'{other_dog.name} has won')
        else:
            print(f'{self.name} has won')

my_dog1 = Dog('Bella', 1, 15)
my_dog2 = Dog('Max', 3, 18)
my_dog3 = Dog('Luna', 2, 20)
my_dog3.fight(my_dog1)
