cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names, heights = zip(*cast)

print(names)
print(heights)

"""
output
('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
(72, 68, 72, 66, 76)
"""
