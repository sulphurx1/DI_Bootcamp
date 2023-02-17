class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

first_cat = Cat('Whiskers', 5)
second_cat = Cat('Felix', 3)
third_cat = Cat('Oscar', 6)

def oldest(*args):
        return max(args)

print(f'The oldest cat is {oldest(first_cat.age, second_cat.age, third_cat.age)} years old')

    
