def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    
    # numeric can be int or float, use tuple to test for both
    if not(isinstance(x, (int, float))) or not(isinstance(y, (int, float))):
        print(-1)
    else:
        x = x + y
        y = x - y
        x = x - y

        print(x, y)


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
# 
swap("Apple", 10)
swap(9, 17)

# References
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/ref_func_isinstance.asp
# https://www.w3schools.com/python/python_operators.asp