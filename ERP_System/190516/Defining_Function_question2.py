def population_density(population,area):
    return population/area

test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))

'''
result
expected result: 10, actual result: 10.0
expected result: 7123.6902801..., actual result: 7123.690280065897
'''
