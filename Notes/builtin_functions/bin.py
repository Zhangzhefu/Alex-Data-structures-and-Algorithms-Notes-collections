"""The bin function converts the given into a binary"""

"""we can add binary like this:"""


def addbinary(a: int, b: int) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]

"""The second parameter in the int function specifies to convert it into base 2
the [2:] is because that all answer after the bin() function because 12b, the 2: removes the b
"""
