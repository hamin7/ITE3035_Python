start_num = 1001  # some start number
end_num = 1000  # some end number that you stop when you hit
count_by = 30  # some number to count by 

# condition to check that end_num is larger than start_num before looping

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    result = break_num

print(result)

# Oops! Looks like your start value is greater than the end value. Please try again.
