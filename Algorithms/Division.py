"""Division in Python"""

"""
Floor division

The floor of a / b is the greatest integer ≤ a / b.

In Python, the operator // is already floor division (not truncation like in some other languages).
"""

print(7 // 3)

"""
Ceiling division
The ceiling of a / b is the smallest integer ≥ a / b.

import math
math.ceil(a / b)   # Generic safe way

(a + b - 1) // b   # Faster integer-only trick
"""

print((7 + 3 - 1) // 3)



