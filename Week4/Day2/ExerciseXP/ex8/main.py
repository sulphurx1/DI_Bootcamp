# declaring the list to store toppings
arr = []

# keep looping the question
while True:
    toppings = input('Please enter your toppings: ')

    #print the previous input from the user
    print(toppings.capitalize() + ' shall be added to your pizza')

    # add the input to the list 
    arr.append(toppings.capitalize())

    # when the user inputs quit as answer
    if(toppings == 'quit'):

        # declaring the last element index
        the_index = (len(arr) - 1)

        # removing quit from the list
        arr.pop(the_index)

        # printing the arr as a single string with joining each element with ',' in between them
        print('The list of toppings on your pizza: ' + ', '.join(arr))

        # calculating the total  price
        total = 10 + (2.5 * (the_index))

        # '%.2f' % total to get exact 2 deciaml place for the price
        print('The total price of your pizza is $' + str('%.2f' % total))

        # to stop the loop from running
        break
