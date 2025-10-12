"""
Binary search is a type of clashing two pointers. It sets up a pointer at left, and a pointer at right. The pointer at
left will move towards the middle by increasing that value, and the pointer at right will move towards the middle
by decreasing its value.

Binary search can only be conducted when the given array is sorted in a certain way.

The biggest difference between binary search and two pointer linear search is:
    - linear search moves only one index each time; eliminating one value at a time.
    - binary search moves from left/right to middle; eliminating half of the values each time
--------------
    - binary search usually has to meet a certain requirement, and at each step they always eliminate 50%
    - linear search just checks for anything that reaches the requirement, and then moves 1 or 2 values inward.
"""

"""
Steps:
    1. define a search space (0 -> len(array) - 1)
    2. find the middle ((left + right) // 2)
    3. compare the middle to the condition
    4. discard one half, if target condition is left half then (right = mid - 1) else (left = mid + 1)
    5. handle edge cases
    
Whenever you see a problem and wonder if binary search applies, ask:

    - Is the data “sorted” or “monotonic” in some way?
    - Can I check a condition at mid that tells me which side to search next?
    - Can I safely discard half of the search space at each step?
    
If the answer is yes → binary search is probably a good fit.
"""


def binary_search(sorted_array, value):
    if not sorted_array:
        return -1

    begin, end = 0,  len(sorted_array) - 1

    while begin <= end:  # 循环
        mid = int((begin + end) / 2)  # 中间段就是 头加尾 除 2
        if sorted_array[mid] == value:  # 如果一切就得到了数值，返回数值
            return mid
        elif sorted_array[mid] < value:  # 如果切后的中间数值大于所需数值，尾 = 中 - 1
            begin = mid + 1
        else:
            end = mid - 1  # 如果切后的中间数值小于所需数值，头 = 中 + 1
    return -1


"""Insert position"""


def binary_search_insert(arr, target):
    left, right = 0, len(arr) - 1
    while right <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


"""Minimum value"""


def binary_search_first_true_pseudocode(low, high, condition):
    """A significant difference is that at the while loop condition, low must be
    smaller than high, it cannot be equal, another issue is that if the value doesn't exist,
    this version has no way of return -1"""
    """pseudocode"""
    while low < high:
        mid = (low + high) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return low


def binary_search_first_true(arr, target):
    """Real code"""
    begin, end = 0, len(arr) - 1
    while begin < end:
        mid = (begin + end) // 2
        if arr[mid] <= target:
            begin = mid
        else:
            end = mid - 1
    return begin


def first_true_II(arr: list[bool]) -> int:
    i, j = 0, len(arr) - 1
    res = -1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid]:
            res = mid
            j = mid - 1
        else:
            i = mid + 1
    return res


"""Max value"""


def binary_search_maximum_k_pseudocode(low, high, condition):
    """pseudocode"""
    while low < high:
        mid = (low + high) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return high


def binary_search_maximum_k(arr, target):
    """Real code"""
    begin, end = 0, len(arr) - 1
    while begin < end:
        mid = (begin + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            begin = mid + 1
    return end
