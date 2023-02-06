answer = input('Please enter a string')

if(len(answer) > 10):
    print('The sring is too long')
elif(len(answer) < 10):
    print('The string is too short')
else:
    # for char in answer:
    #     print(char)
    for i in range(len(answer)):
        print(answer[:i + 1])