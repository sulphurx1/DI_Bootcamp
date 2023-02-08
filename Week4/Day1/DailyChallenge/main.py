answer = input('Please enter a string')

if(len(answer) > 10):
    print('The sring is too long')
elif(len(answer) < 10):
    print('The string is too short')
else:
    # for char in answer:
    #     print(char)
    print(f"{answer[0]}\n{answer[-1]}")

    for i in range(len(answer)):
        print(answer[:i + 1])

    import random
    new_answer = list(answer)
    random.shuffle(new_answer)
    new_answer = ''.join(new_answer)
    print(new_answer)