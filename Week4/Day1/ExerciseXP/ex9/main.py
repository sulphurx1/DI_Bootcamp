height = input('Please enter your height in inches')

convert = float(height) * 2.54

if (convert > 145):
    print('You are tall enough to ride')
else:
    print('You are not tall enough')