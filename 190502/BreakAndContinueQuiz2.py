check_prime = [56, 83, 152, 171, 203, 403, 973]

for num in check_prime:
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
    else:
        print("{} IS a prime number".format(num))

"""
output
56 is NOT a prime number, because 2 is a factor of 56
83 IS a prime number
152 is NOT a prime number, because 2 is a factor of 152
171 is NOT a prime number, because 3 is a factor of 171
203 is NOT a prime number, because 7 is a factor of 203
403 is NOT a prime number, because 13 is a factor of 403
973 is NOT a prime number, because 7 is a factor of 973
"""
