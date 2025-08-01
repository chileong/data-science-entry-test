def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    foundkey = 0
    for x in dct.keys():
        if x == key:
            print(dct[key])
            dct[key] = value
            foundkey = 1

    if (foundkey == 0):
        dct[key] = value

    return dct

print(update_dictionary({},"name","Alice"))
print(update_dictionary({"age":25},"age",26))

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
