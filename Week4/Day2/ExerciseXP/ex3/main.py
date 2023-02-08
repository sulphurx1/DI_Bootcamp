basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# removing banana from array
basket.pop(0)
print(basket)
# removing blueberries from array
basket.pop(-1)
print(basket)
# adding kiwi at the end of the array
basket.append('Kiwi')
print(basket)
#adding apples at the beginning of the set
basket.insert(0, 'Apples')
print(basket)
# how many apples in set
apple = basket.count('Apples')
print(apple)

# to be fixed
######################################
# y = range(0, len(basket))
# z = range(len(basket) - 1, -1, -1)
# count = 0
# for index in y:
#     q = basket[index]
#     for new in z:
#         k = basket[new]
#         if(q == k):
#             print(q)
#             basket.remove(k)
#             count += 1
#             print(count)
######################################
# clearing the basket
clearing = basket.clear()
print(clearing)
