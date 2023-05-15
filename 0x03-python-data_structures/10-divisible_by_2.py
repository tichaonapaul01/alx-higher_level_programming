#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list to store the result
    result = []
    # Iterate through the list and check if each integer is a multiple of 2
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
            # Return the result
    return result
