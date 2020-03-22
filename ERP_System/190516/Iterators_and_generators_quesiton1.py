lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    for i in range(start, len(iterable) + start):
        yield(i, iterable[i-start])
        
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


'''
result
Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
'''
