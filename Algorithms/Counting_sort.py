"""Counting sort"""
"""Counting Sort is a non-comparison-based sorting algorithm that works by counting the frequency of each unique 
element in the input array and then placing them in order. It is efficient when the range of input values (k) is not 
significantly larger than the number of elements (n)."""

"""
Ideal for sorting integers (or objects with integer keys) in a small range.
Used as a subroutine in Radix Sort.

Not suitable for:
Large ranges (e.g., k ≈ n² makes it inefficient).
Floating-point numbers or non-integer data.
"""

"""
Step-by-Step Algorithm
Find the Range:
Determine the min and max values in the input array.
Compute the range: k = max - min + 1.

Initialize Count Array:
Create an array count of size k initialized to 0.
count[i] will store the frequency of the element (i + min).

Populate Counts:
Traverse the input array and increment count[num - min] for each element num.

Compute Cumulative Counts (Prefix Sum):
Modify count such that each count[i] contains the number of elements ≤ (i + min).
This step ensures stability by tracking positions in the output array.

Build the Sorted Output:
Traverse the input array backwards (for stability).
For each element num, place it in output[count[num - min] - 1] and decrement count[num - min].

Copy Back (Optional):
If required, copy the sorted output array back to the original array.
"""


def counting_sort(arr):
    if not arr:
        return arr

    # Step 1: Find the range (min and max)
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1  # Size of count array

    # Step 2: Initialize count array
    count = [0] * k

    # Step 3: Populate counts
    for num in arr:
        count[num - min_val] += 1

    # Step 4: Compute cumulative counts (prefix sum)
    for i in range(1, k):
        count[i] += count[i - 1]

    # Step 5: Build the sorted output
    output = [0] * len(arr)
    for num in reversed(arr):  # Traverse backward for stability
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    # Step 6: Copy back to original array (optional)
    for i in range(len(arr)):
        arr[i] = output[i]

    return arr


"""
Faster than comparison-based sorts (e.g., Merge Sort, Quick Sort) when k = O(n).

Stable and deterministic.

Limitations:
Requires prior knowledge of the data range (k).

Inefficient for large ranges (e.g., k >> n).
"""

"""When the list is compiled with numbers we already know: E.g (0, 1, 2)"""
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """Leetcode 75"""
        count = [0] * 3

        for num in nums:
            count[num] += 1

        index = 0
        for num in range(3):
            for _ in range(count[num]):
                nums[index] = num
                index += 1

