cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(lambda name: len(name)<10, cities))
print(short_cities)

'''
['Chicago', 'Denver', 'Boston']
'''

# highest function == list.
