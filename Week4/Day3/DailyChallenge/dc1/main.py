user_input = input('Please enter a word')
the_dict = {}
for letter_pos, letter in enumerate(user_input):
    if(letter in the_dict.keys()):
        the_dict[letter].append(letter_pos)
    else:
        the_dict[letter] = [letter_pos]
print(the_dict)