user_input = input('Please enter whatever')
remove_duplicate = ''.join(sorted(set(user_input)))
print(remove_duplicate)