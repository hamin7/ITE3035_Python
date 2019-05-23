result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
    for item in fruits:
        #if the key is in the list of fruits, add the value (number of fruits)
        #to result
        if item == key:
            result = result + value

print(result)

# output -> 23
