def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    
    if not(isinstance(s, str)):
        print(-1)
        return
    

    print(s[::-1])


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

string_reverse("Hello World")
string_reverse("Python")

# Reference
# https://www.w3schools.com/python/python_howto_reverse_string.asp