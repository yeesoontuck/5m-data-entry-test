def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    if key in dct:
        print("Original value of " + key + " is: " + str(dct[key]))

    dct[key] = value

    print(dct)


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

update_dictionary({}, "name", "Alice")
update_dictionary({"age": 25}, "age", 26)

# References
# https://www.w3schools.com/python/python_dictionaries_access.asp
# https://www.w3schools.com/python/python_casting.asp
# https://www.w3schools.com/python/python_strings_concatenate.asp