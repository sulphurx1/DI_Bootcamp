sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# targeting the last element of the list and multiple it by 3 and splitting it in a list with ","
x = (sandwich_orders.pop().split(', ')) * 3
# old method to do the same thing as on the top line
# x = (((sandwich_orders)[len(sandwich_orders) -1]).split(',')) * 3

# creating an empty list called finished_sandwich
finished_sandwiches = list()

# looping in the created list x and adding at the end of the "sandwich_order" list
for pastrimi_sandwich in x:
    sandwich_orders.append(pastrimi_sandwich)

# same program from exercise 10
for sandwich in list(sandwich_orders):
    finished_sandwiches.append(sandwich)

    # additional things added
    print('Deli run out of pastrami')

    # while loop for each time "Pastrami sandwich" appear in variable "sandwich", "Pastrami sandwich" will be removed from "sandwich_orders"
    # break added to stop the while loop
    while(sandwich == 'Pastrami sandwich'):
        finished_sandwiches.remove(sandwich)
        break
    print('I made your ' + sandwich)    
print(finished_sandwiches)
    
        
