"""

The XOR operator (^ in Python, C, Java, etc.) is a bitwise operator that operates at the binary level. It compares
corresponding bits of two numbers and returns 1 if the bits are different and 0 if they are the same.

A	B	A ^ B
0	0	0
0	1	1
1	0	1
1	1	0

If both bits are the same -> result is 0
if bits are different -> result is 1
"""

# XORing a number with 0 keeps the number unchanged:
print(5 ^ 0)

# Any number XORed with itself results in 0:
print(5 ^ 5)

# The order of XOR operands DOES NOT matter
print(3 ^ 7)
print(7 ^ 3)

# XOR operations can be grouped in any order without changing the result.
print((2 ^ 3) ^ 4)
print(2 ^ (3 ^ 4))

# If we XOR a number twice the with the same value, we get back the original number.
a = 5
b = 9
a = a ^ b
a = a ^ b

print(a)


