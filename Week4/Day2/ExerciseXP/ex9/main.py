# ask for how many member the family has
member = input('Hello! Please enter the number of member: ')

# converting string to integer 
member = int(member)


count = 0
cost = 0

# loop for the amount of family member   
while(count < member):
    age = input('Please enter the age of each member one by one: ')

    # convert string to integer
    age = int(age)

    # increasing value of count by 1 each time while loop runs
    count += 1

    # condition for different prices
    if(age < 3):
        cost += 0
    elif(age > 2 and age < 13):
        cost += 10
    else:
        cost += 15

# printing out the total amount
print('The total price :$' + str(cost))

# list 
given_names = ['Liam', 'Oliver', 'Benjamin', 'Lucas', 'William']

# looping through list 
for name in given_names:

    # asking for the age of each person
    age = input('Please enter the age of ' + name)
    age = int(age)
    if(age > 15 and age < 22):
        cost += 15
    else:
        given_names.pop(name)
print(given_names)
print('The total price :$' + str(cost))