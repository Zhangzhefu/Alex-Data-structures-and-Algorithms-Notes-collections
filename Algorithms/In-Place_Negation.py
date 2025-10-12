"""
In-place negation is a programming trick where you negate (flip the sign)
of elements in a list or array without using extra memory — you perform operations within the original array itself,
modifying its values directly.

+++++++++++++++++++++++++
It's commonly used to:

Mark visited elements

Track presence of values

Encode binary states (visited/unvisited, yes/no)

+++++++++++++++++++++++++

It works because in python for example, numbers are mutable when stored in a list
Negating a number (x -> -x) preserves the magnitude but encodes a signal in the sign.
"""


def missing_numbers_in_range(nums: list[int]) -> list[int]:
    for num in nums:
        index = abs(num) - 1  # ensures we use the original number, even if it's been negated already
        nums[index] = -abs(nums[index])  # sets the value at that position to negative, marking "visited"

    return [i + 1 for i, num in enumerate(nums) if num > 0]  # look for the numbers that are still positive


def find_duplicates(nums):
    """First time we see x, we mark nums[x-1] as negative
Second time we see x, nums[x-1] is already negative → duplicate!"""
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]
    return result
