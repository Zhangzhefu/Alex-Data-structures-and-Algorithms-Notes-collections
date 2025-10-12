from __future__ import annotations
from typing import Optional

"""
Recursion:

1. Starting with the recurrence relation
    - Base case?? For what problem?
    - Actions               --> Recursive calls
    - Consequences          --> Transitions
    - Contributions         --> Return Value
    - Affected variables    --> Parameters

2. Obey the rules of recursion:
    1. Base case must be correct
    2. Recursive calls shrink to a basecase
    3. Assume recursive calls are correct

3. Builds base cases from the calls
    - Name the function on it's promise!
    - Avoid simulating/visualizing, it's painful
    - Recursion is naturally inductive
    - Read aloud and see if it makes sense

4. Main Ideas:
     Structure --> Technique
     
     Recursion:
        Where: Subtasks have the same shape
        Why: To simplify a problem with induction
        How: Use induction!!
    
    Don't think more than 1 recurrence down name a function on it promises to do.
    No prints or simulation, just read it aloud.
"""


class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


# def includes(haystack: Optional[Node], needle: int) -> bool:
#     """Is needle in the haystack"""
#     if haystack is None:
#         return False
#     elif haystack.data == needle:
#         return True
#     else:
#         return includes(haystack.next, needle)


# def is_equal(a: Optional[Node], b: Optional[Node]) -> bool:
#     """Are a and b equal"""
#     if a is None and b is None:
#         return True
#     elif a is None or b is None:
#         return False
#     elif a.data != b.data:
#         return False
#     else:   # Both datas are equal
#         return is_equal(a.next, b.next)


# def seq(low: int, high: int) -> Optional[Node]:
#     """Return sequence of nodes between low and high, not inclusive of high"""
#     # if low == high:
#     #     return None
#     # elif low > high:
#     #     return None
#     if low >= high:
#         return None  # This combined the 2 conditions above
#     else:
#         # subproblem: int = low
#         # rest: Optional[Node] = seq(low+1, high)
#         # return Node(subproblem, rest)
#         return Node(low, seq(low+1, high))   # This combined the 3 lines above


# def sum_of_list(a):
#     if len(a) == 1:
#         return a[0]
#     else:
#         return a[0] + sum_of_list(a[1:])
#
#
# print(sum_of_list([2, 3, 4, 5, 6]))


# def convert_str(a, base):
#     convert = "0123456789ABCDEF"
#     if a < base:
#         return convert[a]
#     else:
#         return convert_str(a // base, base) + convert[a % base]
#
#
# print(convert_str(2835, 16))

# def listFlaten(array):
#     for i in array:
#         if type(i) == int:
#             outputlist.append(i)
#         elif type(i) == list:
#             listFlaten(i)
#     return outputlist
#
# outputlist = []
#
# toFlatten = [1, [1, [[[[5]]], 2]]]
# print(listFlaten(toFlatten))


# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
#
#
# print(factorial(4))

# def sum_list(array):
#     sum = 0
#     for i in array:
#         if type(i) == int:
#             sum += i
#         else:
#             sum += sum_list(i)
#     return sum
#
#
# arr = [1, 2, [3, 4], [5, 6]]
# print(sum_list(arr))


# def fibonacci(array):
#     if array == 1 or array == 2:
#         return 1
#     else:
#         return fibonacci(array - 1) + fibonacci(array - 2)
#
#
# print(fibonacci(10))


def print_num(n: int):
    """As long as you don't return, it doesn't exit the function
    if print is before recursive call, it prints every value before recursing
    if print is after recursive, it starts to print once it reaches the base case
    """
    if n == 0:
        return
    else:
        print_num(n - 1)
        print(n)
        # return v
        # print(n)
        # return print_num(n-1)


print_num(10)

