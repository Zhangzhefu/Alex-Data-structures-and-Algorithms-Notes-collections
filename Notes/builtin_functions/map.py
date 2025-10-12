# how does the function map() work? The map() function in Python is used to apply a specified function to each item
# in an iterable (like a list, tuple, etc.) and returns a map object (which is an iterator). This is particularly
# useful for transforming data in a concise and readable way.
#
# Syntax
# The basic syntax of map() is:
#
# map(function, iterable, ...)
# function: A function that you want to apply to each element of the iterable.
#
# iterable: One or more iterable(s) whose elements are passed to the function.
#
# map(a, b)
# Basically the map() function does this function(a) to this iterable(b)
#
# example:
def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]

# Apply the function to each element using map()
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # Outputs: [1, 4, 9, 16, 25]

# Using lambda:
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() with a lambda function
squared_numbers = map(lambda x: x ** 2, numbers)

# Convert the map object to a list and print it
print(list(squared_numbers))  # Outputs: [1, 4, 9, 16, 25]


# same function, but way less code！
#
# Example with Multiple Iterables If you provide multiple iterables to map(), the function will apply to
# corresponding elements from each iterable in parallel:
#
# python
# Define a function that adds two numbers
def add(x, y):
    return x + y


# Create two lists of numbers
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Use map() to add corresponding elements
added_numbers = map(add, list1, list2)

# Convert the map object to a list and print it
print(list(added_numbers))  # Outputs: [5, 7, 9]
