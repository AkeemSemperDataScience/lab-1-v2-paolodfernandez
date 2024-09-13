def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = input_gb * 1024 * 1024 * 1024
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    return num_bytes
lab1Question1(1)

def lab1Question2(name):
    is_odd = None
    length = len(name)
    if length % 2 == 1:
        is_odd = True
    else: is_odd = False

    return is_odd

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    if 0 <= input_number < len(input_string):
        character_at = input_string[input_number]
    else: character_at = -1
    return character_at

def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    for numbers in file_name:
        if numbers in "123456789":
            list_of_nums.append(numbers)
            
    return list_of_nums

def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    mode_of_list = None
    if not list_numbers:
        return None
    frequency = {}
    for num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
    max_count = max(frequency.values())
    mode_of_list = [num for num, freq in frequency.items() if freq == max_count]
    if len(mode_of_list) == 1:
        return mode_of_list[0]
    else:
        return mode_of_list

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None
    value_quarter = 0.25
    value_dime = 0.10
    value_nickel = 0.05
    value_penny = 0.01
    total = (quarters * value_quarter + dimes * value_dime + nickels * value_nickel + pennies * value_penny)
    return total

## Example of calling a function to test these... 
# Question 1 Check:
in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.