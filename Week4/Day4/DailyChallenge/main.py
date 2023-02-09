matrix = ['7i3', 'Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', '^r!']

matrix = list(zip(*matrix))
print(matrix)

string = ''
for index in matrix:
    string = string + ''.join(index)

print(string)

import re
string = re.sub(r"\b[^a-zA-Z0-9]+\b", r" ",string)

print(string)