def rotate_matrix_inplace(matrix):
    n = len(matrix)  # Size of the matrix

    # Iterate through each layer (outer to inner)
    for p in range(3):
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                # Perform a 4-way swap
                temp = matrix[i][j]  # Store top-left element

                # Move bottom-left to top-left
                matrix[i][j] = matrix[n - j - 1][i]

                # Move bottom-right to bottom-left
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

                # Move top-right to bottom-right
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

                # Move top-left (saved in temp) to top-right
                matrix[j][n - i - 1] = temp


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:2}" for num in row))


matrix = [
    [3, 7, 9],
    [2, 5, 6],
    [1, 3, 4]
]

print("Original Matrix:")
print_matrix(matrix)

rotate_matrix_inplace(matrix)

print("\nRotated Matrix (90° Clockwise):")
print_matrix(matrix)
"""
n - j - 1 = 2, 1 based on what j is. (j=0, answer=2) (j=1, answer= 1)
n - i - 1 =  2.
Sometimes the variable that is higher in value is needed, that's why n-i-1 is needed. n-j-1 is when the values move.

j has always one more value than i does.

The reason the first for loop was n // 2 was because, there are only a certain amount of rotations needed. 
When the 2D-Array 3 by 3, there are only 2 rotations needed, that being corners and middle. i has the value of 0,
j has the value of 0, 1. Because i is the constant, and j is the variable.
When 2D-Array is 4 by 4, there are only 3 rotations needed being the, 2 middle and the corners. i can be 0, 1,
j has the value of 0, 1, 2. Because i is the constant, and j is the variable.

starts by saving the value of the origin in a variable temp. Points the value of bottom left to top left, resulting in
bottom left being empty. Then point bottom right value to bottom left resulting in bottom right being empty. Then point
top right value to bottom right resulting top right being empty. Point value in temp to top right to finish the rotation
"""

# +++++++++++++++++++++++

"""
n - j - 1 is used to access the opposite row (bottom → top).
n - i - 1 is used to access the opposite column (right → left).


Why n - j - 1?
Since indices range from 0 to N-1, subtracting j from N-1 finds the corresponding opposite index.
For example:

In a 3×3 matrix (n=3):
j = 0 → n - j - 1 = 3 - 0 - 1 = 2
j = 1 → n - j - 1 = 3 - 1 - 1 = 1
Thus, we can directly reference the opposite side.
"""
