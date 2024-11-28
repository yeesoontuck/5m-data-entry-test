def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    if not(isinstance(lst, list)):
        print("Input is not a list")
        return
    
    newlist = []

    for x in lst:
        if x == find_val:
            x = replace_val
        newlist.append(x)
    
    print(newlist)

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
find_and_replace(["apple", "banana", "apple"], "apple", "orange")

# References
# https://www.w3schools.com/python/python_lists_comprehension.asp
# https://www.w3schools.com/python/python_lists.asp
# https://www.w3schools.com/python/python_lists_add.asp