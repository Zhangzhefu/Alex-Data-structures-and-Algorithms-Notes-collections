number_list = [0, 1, 2, 3, 4, 5, 6, 7]


def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1


assert linear_search(5, number_list) == 5


def linear_search_lambda(predicate, iterable):
    for index, value in (predicate, iterable):
        if predicate(value):
            return index
    return -1


assert linear_search_lambda(lambda x: x == 5, number_list) == 5


def linear_search_recursive(array, value):
    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    return linear_search_recursive(array[0:index], value)

