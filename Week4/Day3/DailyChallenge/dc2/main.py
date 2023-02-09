# dictionary // list of items
items_purchase = {
    'Water': '$1',
    'Bread': '$3',
    'TV': '$1,000',
    'Fertilizer': '$20'
}

# declaring value for wallet
wallet = '$300'

# converting string value of wallet to integer as comparing was not working and removing "$" symbol
wallet = int(wallet.replace('$', ''))

# looping through dictionary with list to make a copy of the dictionary or error: the size of the dictionary, will be encounter
for item in list(items_purchase):

    # converting string value of price to integer as comparing was not working and removing "$" symbol
    # getting value with .get(item)
    price = int(items_purchase.get(item).replace('$', '').replace(',', ''))

    # if the price of the product is higher than wallet pop that item from dictionary
    if(price > wallet):
        items_purchase.pop(item)

# if the length of the dictionary is "0" print: Nothing        
if(len(items_purchase) == 0):
    print('Nothing')

# printing the list of item purchasale
print(sorted(items_purchase.keys()))

