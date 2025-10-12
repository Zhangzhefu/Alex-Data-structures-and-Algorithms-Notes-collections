# def binary_search(sorted_array, value):
#     if not sorted_array:
#         return -1
#
#     begin = 0
#     end = len(sorted_array) - 1
#
#     while begin <= end:  # 循环
#         mid = int((begin + end) / 2)  # 中间段就是 头加尾 除 2
#         if sorted_array[mid] == value:  # 如果一切就得到了数值，返回数值
#             return mid
#         elif sorted_array[mid] > value:  # 如果切后的中间数值大于所需数值，尾 = 中 - 1
#             end = mid - 1
#         else:
#             begin = mid + 1  # 如果切后的中间数值小于所需数值，头 = 中 + 1
#     return -1
#
#
# def test_binary_search():
#     a = list(range(10))
#
#     assert binary_search(a, 1) == 1
#     assert binary_search(a, -1) == -1
#
#     assert binary_search(None, 1) == -1
#
#     assert binary_search(a, 0) == 0

def binary_search(sorted_array, value):
    if not sorted_array:
        return -1

    begin = 0
    end = len(sorted_array) - 1

    while begin <= end:
        mid = int((begin + end) // 2)
        if sorted_array[mid] == value:
            return mid
        elif sorted_array[mid] > value:
            end = mid - 1
        else:
            begin = mid + 1
    return -1


"""Generalized Binary search"""


def binary_search_first_true(low, high, condition):
    """A significant difference is that at the while loop condition, low must be
    smaller than high, it cannot be equal, another issue is that if the value doesn't exist,
    this version has no way of return -1"""
    while low < high:
        mid = (low + high) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return low


"""For maximum k such that condition(k) is True"""


def binary_search_maximum_k(low, high, condition):
    while low < high:
        mid = (low + high) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return high


def bin_search(arr, target):
    if not arr:
        return -1
    low, high = 0, len(arr)

    while low < high:
        mid = low + (high - low) // 2
        # mid = int(high - low) // 2
        if arr[mid] == target:
            high = mid
        else:
            low = mid + 1
    return low


l1 = [1, 2, 3, 4, 5]
print(bin_search(l1, 3))