#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    
    # Psuedocode:
    # 1. Use the range() function to create a range of user-defined integers.
    # 2. Wrap the range() function around the parameter of the user-defined calculate_sum()
    #    function.
    # 3. Since the end value of the range() parameter must be inclusive
    #    (the default is exclusive), add 1 to the 'end' parameter.
    # 4. Wrap the parameter and the range() function with the sum() function.
    # 5. Assign the logic above to the variable 'my_sum'.
    # 6. Use a return statement to return 'my_sum', which contains the calculated
    #    sum of the range of values. 
    
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    my_sum = sum(range(start, end + 1))
    
    # TODO: Return the calculated sum.
    return my_sum

# answer_1 = calculate_sum(1, 6)
# print(answer_1)

def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """

    # Psuedocode:
    # 1. Use the range() function to create a range of user-defined integers.
    # 2. Wrap the range() function around the parameter of the user-defined
    #    find_smallest_number() function.
    # 3. Since the end value of the range() parameter must be inclusive
    #    (the default is exclusive), add 1 to the 'end' parameter.
    # 4. Wrap the parameter and the range() function with the min() function.
    # 5. Assign the logic above to the variable 'smallest_num'.
    # 6. Use a return statement to return 'smallest_num', which contains the minimum
    #    value in the range. 

    # TODO: Implement the logic to find the smallest number within the range.
    smallest_num = min(range(start, end + 1))
    # TODO: Return the found smallest number.
    return smallest_num

# smallest_int = find_smallest_number(8, 275)
# print(smallest_int)


def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """

    # Psuedocode:
    # 1. Use the range() function to create a range of user-defined integers.
    # 2. Wrap the range() function around the parameter of the user-defined
    #    find_largest_number() function.
    # 3. Since the end value of the range() parameter must be inclusive
    #    (the default is exclusive), add 1 to the 'end' parameter.
    # 4. Wrap the parameter and the range() function with the max() function.
    # 5. Assign the logic above to the variable 'smallest_num'.
    # 6. Use a return statement to return 'largest_num', which contains the maximum
    #    value in the range. 

    # TODO: Implement the logic to find the largest number within the range.
    largest_num = max(range(start, end + 1))
    # TODO: Return the found largest number.
    return largest_num


# largest_int = find_largest_number(12, 74)
# print(largest_int)

def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """

    # Psuedocode:
    # 1. Set to zero the accumulator variable, 'count_even_num'.
    # 2. Use the range() function to create a range of user-defined integers.
    # 3. Wrap the range() function around the parameter of the user-defined
    #    count_even_numbers() function.
    # 3. Since the end value of the range() parameter must be inclusive
    #    (the default is exclusive), add 1 to the 'end' parameter.
    # 4. Use a 'for' loop to iterate through the range of values.
    # 5. Within the 'for' loop, nest an if/else statement that increments the
    #    accumulator by one each time the iterated value is divided evenly by 2.
    #    Else, do not increment the accumulator, and continue by evaluating
    #    the next number in the range.
    # 6. Use a return statement to return 'count_even_num', which contains the count
    #    of the even values in the range.

    # TODO: Implement the logic to count even numbers within the range.
    count_even_num = 0
    even_values = range(start, end + 1)
    
    for value in even_values:
        if value % 2 == 0:
            count_even_num += 1
        else:
            continue
    
     # TODO: Return the count of even numbers.
    return count_even_num


# even_ints = count_even_numbers(5, 315)
# print(even_ints)

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """

    # Psuedocode:
    # 1. Set to zero the accumulator variable, 'count_odd_num'.
    # 2. Use the range() function to create a range of user-defined integers.
    # 3. Wrap the range() function around the parameter of the user-defined
    #    count_odd_numbers() function.
    # 3. Since the end value of the range() parameter must be inclusive
    #    (the default is exclusive), add 1 to the 'end' parameter.
    # 4. Use a 'for' loop to iterate through the range of values.
    # 5. Within the 'for' loop, nest an if/else statement that increments the
    #    accumulator by one each time the iterated value is not divided evenly by 2.
    #    Else, do not increment the accumulator, and continue by evaluating
    #    the next number in the range.
    # 6. Use a return statement to return 'count_odd_num', which contains the count
    #    of the odd values in the range.
    
    # TODO: Implement the logic to count odd numbers within the range.
    count_odd_num = 0
    odd_values = range(start, end + 1)
    
    for value in odd_values:
        if value % 2 != 0:
            count_odd_num += 1
        else:
            continue
    # TODO: Return the count of odd numbers.
    return count_odd_num

# odd_ints = count_odd_numbers(1, 12)
# print(odd_ints)