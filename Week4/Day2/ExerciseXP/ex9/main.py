member, answer = input('Hello! Please enter the number of member and the type of movies you wish to watch (special or normal): ').split(' ')
names = []
count = 0
cost = 0
    

while (answer == 'special'):
    name, ask_age = input('Please enter the name and age of each person: ').split(' ')
    names.append(name)
    ask_age = int(ask_age)
    if(ask_age > 15 and ask_age <= 21):
        cost += 15
    count += 1
    if(count == int(member)):
        print(names)
        print('Total price: $' + str(cost))
        break
    else:
        names.remove(name)
while (answer == 'normal'):
    ask_age = input('Please enter the age of each person: ')
    int(ask_age)
    if(ask_age < 3):
        None
    elif(ask_age > 2 and ask_age < 12):
        cost += 10
    else:
        cost += 15
    count += 1
    if(count == int(member)):
        print('Total price: $' + str(cost))
        break



 
