'''Write a function named readable_timedelta. The function should take one argument, an integer
days, and return a string that says how many weeks and days that is. For example, readable_timedelta(10)
should return, 1 week(s) and 3 day(s).'''

def readable_timedelta(days):
    """Print the number of weeks and days in a number of days."""
    #to get the number of weeks we use integer division
    weeks = days // 7
    #to get the number of days that remain we use %, the modulus operator
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

print(readable_timedelta(10))


'''
result
1 week(s) and 3 day(s)
'''

    
