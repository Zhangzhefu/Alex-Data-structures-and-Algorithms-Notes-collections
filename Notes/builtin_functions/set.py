# The set() function in Python is used to create a set, which is an unordered collection of unique elements. Sets are
# particularly useful when you need to eliminate duplicates or perform mathematical set operations like union,
# intersection, or difference.
#
# Key Properties of Sets
# Unordered: Sets do not preserve the order of elements.
# Unique Elements: Duplicate values are automatically removed.
# Mutable: You can add or remove elements from a set.
# Iterable: You can loop through a set.
#

# Example:
# From a list
numbers = [1, 2, 3, 2, 1]
unique_numbers = set(numbers)
print(unique_numbers)

# the answer would be:
{1, 2, 3}