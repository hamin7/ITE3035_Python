multiples_3 = [ x for x in range(3, 60+1)  if x % 3 == 0]
print(multiples_3)

"""
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
"""

# Second solution:

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)
