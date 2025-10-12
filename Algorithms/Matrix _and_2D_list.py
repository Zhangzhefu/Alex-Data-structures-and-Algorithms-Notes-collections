class Solution1:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        matrix_size = len(matrix)
        if matrix_size == 1:
            curr_row = 0
            i, j = 0, len(matrix[curr_row]) - 1
            while i <= j:
                if matrix[curr_row][i] == target or matrix[curr_row][j] == target:
                    return True
                i += 1
                j -= 1
            return False

        curr_row = matrix_size // 2
        while 0 <= curr_row <= matrix_size - 1:
            if target < matrix[curr_row][0]:
                curr_row -= 1
                if curr_row < 0 or target > matrix[curr_row][-1]:
                    return False

            elif target > matrix[curr_row][-1]:
                curr_row += 1
                if curr_row > matrix_size - 1 or target < matrix[curr_row][0]:
                    return False

            else:
                i, j = 0, len(matrix[curr_row]) - 1
                while i <= j:
                    if matrix[curr_row][i] == target or matrix[curr_row][j] == target:
                        return True
                    i += 1
                    j -= 1
                return False


class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        flattened_list = []

        def flatten(array):
            for i in array:
                if type(i) == int:
                    flattened_list.append(i)
                if type(i) == list:
                    flatten(i)
            return flattened_list

        flatten(matrix)

        begin, end = 0, len(flattened_list) - 1
        while begin <= end:
            mid = int(begin + end) // 2
            if flattened_list[mid] == target:
                return True
            elif flattened_list[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1

        return False


"""Leetcode 240: Search 2D matrix II"""


class Solution3:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """My original code"""
        matrix_size = len(matrix)
        if matrix_size == 1:
            curr_row = 0
            left, right = 0, len(matrix[curr_row]) - 1
            while left <= right:
                mid = int((left + right) // 2)
                if matrix[curr_row][mid] == target:
                    return True
                elif matrix[curr_row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        elif len(matrix[0]) == 1:
            curr_col = 0
            top, bottom = 0, len(matrix) - 1
            while top <= bottom:
                mid = int((top + bottom) // 2)
                if matrix[mid][curr_col] == target:
                    return True
                elif matrix[mid][curr_col] < target:
                    top = mid + 1
                else:
                    bottom = mid - 1
            return False

        curr_row = 0
        curr_col = 0
        while curr_col < matrix_size - 1 and curr_row < len(matrix[0]) - 1:
            left, right = curr_col, len(matrix[curr_row]) - 1
            while left <= right:
                mid = int((left + right) // 2)
                if matrix[curr_row][mid] == target:
                    return True
                elif matrix[curr_row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            top, bottom = curr_row, len(matrix) - 1
            while top <= bottom:
                mid = int((top + bottom) // 2)
                if matrix[mid][curr_col] == target:
                    return True
                elif matrix[mid][curr_col] < target:
                    top = mid + 1
                else:
                    bottom = mid - 1

            curr_col += 1
            curr_row += 1
        return True if matrix[-1][-1] == target else False


"""2D list and 1D list"""

"""
matrix = [
  [ 1,  3,  5],
  [ 7,  9, 11],
  [13, 15, 17]
]

m = 3 rows
n = 3 columns
if we flattened it, it looks like:
[1, 3, 5, 7, 9, 11, 13, 15, 17]

"""

"""
There is a mapping formula
Every element in the 1D flattened array can be mapped back to (row, col) using division and modulus

Given 1D index -> 2D coordinates:
    row = index / n, col = index % n

Given 2D coordinates -> 1D index:
    index = row * n + col
    
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, n)     # convert 1D index → 2D
        val = matrix[row][col]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

