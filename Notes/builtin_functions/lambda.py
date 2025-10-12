# In Python, a lambda function is a small anonymous function defined using the lambda keyword. Unlike regular
# functions that are defined using the def keyword, lambda functions are defined inline and are often used for short,
# simple operations.
#
# Basic Syntax
# The syntax for a lambda function is:
#
#
# lambda arguments: expression
# lambda: The keyword to define a lambda function.
#
# arguments: A comma-separated list of arguments.
#
# expression: A single expression to be evaluated and returned.
#
# example:

add = lambda x, y: x + y
print(add(2, 3))  # Outputs: 5

# add is a lambda function that takes two arguments, x and y.
#
# The expression x + y is evaluated and returned.


def average(l, op):
    def sum_rec(arr) -> int:
        """Nested recursion"""
        if not arr:
            return 0
        return arr[0] + sum_rec(arr[1:])

    if not l:
        return 0
    return op(sum_rec(l), len(l))  # calling lambda function


l1 = [1, 2, 3, 4, 5]
print(average(l1, lambda a, b: a // b))  # Defining lambda function
