# Create a table (i.e. a 2d array) of size M x N filled with random integers between 1 and 100,where 1 < N < 40 and 1 < M < 50.
import numpy as np
import random

N = random.randint(1, 40)
M = random.randint(1,50)

a = np.arange(M * N).reshape((M,N))
print(f'{M} & {N}')
# print(a)
#
#
# Print out the third row
third_row = a[2, :]
# print(third_row)
#
#
# Print out the third column
third_column = a[:, 2]
# print(third_column)
#
#
# Set every element in the last row equal to 7
# repeating 7 for N amount of times
x = [7] * N

#replacing the last row with 7
a[M - 1, :] = x
#
#
# Set every element in the last column equal the sum of the first two columns
# summation of all column
all_sum = np.sum(a, axis = 0)

#summation of 1st and 2nd column
the_element = all_sum[0] + all_sum[1]

# repeat the value for M amount of rows
y = [the_element] * M

# replacing last column with value
a[:, N - 1] = y







