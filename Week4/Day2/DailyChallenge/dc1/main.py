number, length = input('Please enter a number and a length').split()
arr =[]
number = int(number)
y = range(1, int(length) + 1)
for num in y:
    calc = number * num
    arr.append(calc)
print(arr)