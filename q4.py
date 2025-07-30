def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    new=""
    length = len(s)
    for x in range(length):
        new = new + s[length - x - 1]
        
    return new

print(string_reverse("Hello World"))
print(string_reverse("python"))
# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
