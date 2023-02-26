import random
print
def random_number():
    x = int(input('Please enter a number between 1 and 100: '))
    if(x > 0 and x <= 100):
        y = random.randint(1, 100)
        if(x == y):
            print(f'Success!')
        else:
            print(f'Fail! input value: {x} and random value: {y}')
    else: 
        print(f'the input value is not between 1 and 100')    

random_number()