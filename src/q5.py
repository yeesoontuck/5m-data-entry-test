def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    # modulus returns 0 if it is divisible
    return (num % divisor) == 0
    # return True


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(check_divisibility(10, 2))
print(check_divisibility(7, 3))

# Reference
# https://www.w3schools.com/python/python_operators.asp