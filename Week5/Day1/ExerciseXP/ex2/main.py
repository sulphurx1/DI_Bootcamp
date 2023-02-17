class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!") 

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x}cm high!") 


davids_dog = Dog('Rex', 50)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
sarahs_dog.bark()
sarahs_dog.jump()


def bigger():
    if(sarahs_dog.height > davids_dog.height):
        print(f'{sarahs_dog.name} is the bigger dog')
    else:
        print(f'{davids_dog.name} is the bigger dog')

        
bigger()








