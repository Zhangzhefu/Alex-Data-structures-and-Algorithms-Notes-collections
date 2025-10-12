# The digital root of a number is the single-digit value you get by repeatedly summing the digits of the number until
# only one digit remains.

"""
It turns out that the digital root of a number is the same as num % 9, with a slight adjustment:

If num == 0, digital root is 0.

Otherwise, digital root is 1 + (num - 1) % 9.

Why does this work?
It's based on a mathematical property in base-10:

A number and the sum of its digits are congruent modulo 9.

"""

"""
Why 1 + (num - 1) % 9 instead of num % 9?
Because when num is a multiple of 9, num % 9 = 0, but its digital root should be 9, not 0.

This small shift (-1 and +1) corrects that:

If num = 9: 1 + (9 - 1) % 9 = 1 + 8 % 9 = 1 + 8 = 9

If num = 18: 1 + (17 % 9) = 1 + 8 = 9

"""


def Digital_Roots(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9
