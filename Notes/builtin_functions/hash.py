# The hash() function in Python returns the hash value of an object (if it has one). Hash values are integers used to
# quickly compare dictionary keys during a dictionary lookup. Essentially, a hash value is a numeric representation
# of an object's data.
#
# Deterministic: The hash() function is deterministic. This means that for the same input, it will always produce the
# same output within a single execution of a program. However, the hash values may differ between different runs of
# the program.
#
# Immutable Objects: The hash() function can only be used on immutable objects such as strings, numbers, and tuples.
# Mutable objects, like lists and dictionaries, do not have a hash value.
#
# Implementation: Under the hood, Python uses various algorithms to compute hash values based on the type of the
# object. For example, the algorithm used to hash strings is different from the one used to hash tuples.
#
# Practical Use Cases Dictionaries: Hash values are primarily used in dictionaries. When you use a key to access a
# value in a dictionary, Python computes the hash of the key to quickly find the corresponding value.
#
# Sets: Hash values are also used in sets to efficiently manage and look up elements.
