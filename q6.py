def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    for x in lst:
        if(x < 0):
            return x
    return "No negatives"

lst1 = [3, 5, -1, 7, -2, 8]
lst2 = [2, 10, 7, 0]

print(find_first_negative(lst1))
print(find_first_negative(lst2))

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
