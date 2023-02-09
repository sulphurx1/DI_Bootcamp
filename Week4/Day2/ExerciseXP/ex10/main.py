sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = list()

for sandwich in list(sandwich_orders):
    finished_sandwiches.append(sandwich)
    if(len(finished_sandwiches) == len(sandwich_orders)):
        for finish in list(finished_sandwiches):
            print('I made your ' + finish)

