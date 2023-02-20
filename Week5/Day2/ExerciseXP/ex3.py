from ex2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        Dog.__init__(self, name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f'{args} all play together')

    def do_a_trick(self):
        if self.trained == True:
            print(f'{self.name} ' + the_list[x])

        else:
            pass

x = random.randint(0, 3)
the_list = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']

my_dog = PetDog('Bella', 5, 15)