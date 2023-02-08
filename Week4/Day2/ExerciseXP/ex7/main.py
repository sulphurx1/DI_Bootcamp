arr = []
# ask for user input data
fruits_list = input('Please enter a list of fruits: ').split()
# to store input into a list
for fruit in fruits_list:
    arr.append(fruit)
print(arr)

is_it_fruit = input('Please enter a fruit: ')
# for index in range(0, (len(arr) - 1)):
#     if(is_it_fruit == arr[index]):
#         print('You chose one of your favorite fruits! Enjoy!')
#         break
#     else:
#         print('You chose a new fruit. I hope you enjoy')
#         break
if is_it_fruit in arr:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')
