# def quicksort(array):
#     if len(array) < 2:
#         return array
#     pivot_index = 0
#     pivot = array[pivot_index]
#     less_part = [array[i] for i in range(len(array)) if array[i] <= pivot and pivot_index != i]
#     great_part = [array[i] for i in range(len(array)) if array[i] > pivot and pivot_index != i]
#     return quicksort(less_part) + [pivot] + quicksort(great_part)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]  # Choose the pivot (first element)
#   Partition the array into less and greater parts
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
#   Recursively sort and combine
    return quicksort(less) + [pivot] + quicksort(greater)


def quicksort_test():
    # import random
    # seq = list(range(10))
    # random.shuffle(seq)
    # assert quicksort(seq) == sorted(seq)
    unsorted = ["6", "31415926535897932384626433832795", "1", "3", "10", "3", "5"]
    for i in range(len(unsorted)):
        unsorted[i] = int(unsorted[i])

    quicksort(unsorted)


# def partition(array, start, end):
#     pivot_index = start
#     pivot = array[pivot_index]
#     left = pivot_index + 1
#     right = end - 1
#
#     while True:
#         while left <= right and array[left] < pivot:
#             left += 1
#
#         while right >= left and array[right] >= pivot:
#             right -= 1
#
#         if left > right:
#             break
#         else:
#             array[left], array[right] = array[right], array[left]
#
#     array[pivot_index], array[right] = array[right], array[pivot_index]
#     return right


# def test_partition():
#     l = [4, 1, 2, 8]
#     assert partition(l, 0, len(l)) == 2
#     g = [1, 2, 3, 4]
#     assert partition(g, 0, len(l)) == 0
#     f = [4, 3, 2, 1]
#     assert partition(f, 0, len(l)) == 3


# def quicksort_inplace(array, start, end):  # 左闭右开区间
#     if start < end:
#         pivot = partition(array, start, end)
#         quicksort_inplace(array, start, pivot)
#         quicksort_inplace(array, pivot+1, end)


# def test_quicksort_inplace():
#     import random
#     seq = list(range(10))
#     random.shuffle(seq)
#     print(seq)
#     quicksort_inplace(seq, 0, len(seq))
#     print(seq)
