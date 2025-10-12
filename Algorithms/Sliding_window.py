"""
The sliding window technique is an algorithmic approach used to
efficiently solve problems involving arrays or lists where you need to find a subset of elements
that satisfy certain conditions. It's particularly useful for problems involving contiguous sub-arrays or substrings.

=======================

Fixed-size window: The window maintains a constant size as it slides

Variable-size window: The window can grow or shrink based on certain conditions

Efficiency: Typically reduces time complexity from O(n²) to O(n)

========================

Initialize pointers or variables to represent the window boundaries (usually left and right)

Expand the window by moving the right pointer

Shrink the window (if needed) by moving the left pointer

Track the required information (sum, count, etc.) as the window moves
"""

"""
To this time, I've done a lot of sliding window problems, and I am fairly good at solving them now
If I forget how to in the future, go to leetcode sliding window, all my solutions are there
"""


# Fixed-Size Window example (Leetcode 643)


def find_max_average(nums, k):
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window from k to end of array
    for i in range(k, len(nums)):
        # Subtract the element going out of window
        # Add the new element coming into window
        window_sum += nums[i] - nums[i - k]

        # Update max_sum if current window_sum is greater
        max_sum = max(max_sum, window_sum)

    return max_sum / k


def fixed_window(arr, k):
    """Constant-sized window"""
    n = len(arr)
    res = 0   # depends on problem: sum, max, min, etc.
    window_sum = 0

    # initialize first window
    for i in range(k):
        window_sum += arr[i]
    res = window_sum

    # slide the window
    for right in range(k, n):
        window_sum += arr[right]          # add new element
        window_sum -= arr[right - k]      # remove leftmost element
        res = max(res, window_sum)        # update result
    return res


def variable_window(arr, condition):
    """Variable-sized window"""
    n = len(arr)
    left = 0
    res = 0

    # data structure to track state
    freq = {}

    for right in range(n):
        # expand window
        # This simply adds the new element into the current dictionary
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        # shrink until condition is satisfied
        while not condition(freq):
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:  # If there is none left, remove it
                del freq[arr[left]]
            left += 1  # Move left pointer forward

        # update result (depends on problem)
        res = max(res, right - left + 1)
        # right-left+1 is the formula for current window size

    return res


# Variable-size window example (Longest substring without repeating characters)


def longest_substring_without_repeating(s):
    char_set = set()
    # We maintain a set to track characters in current window
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Expand window by moving right pointer
        while s[right] in char_set:
            # If we encounter a duplicate character, shrink window from left until no duplicates
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        # Expand window by moving right pointer
        max_length = max(max_length, right - left + 1)
        # Track maximum window size (substring length) found

    return max_length


"""
^^^ Sliding window for longest substring without repeating characters ^^^

The goal: FInd the length of the longest substring of s without duplicating characters

INPUT: s = "abcabcbb"
OUTPUT: 3

Solution:
1. Expand right until duplicate is found
2. Shrink left to remove duplicates
3. Track maximal window size

Pitfalls:
Subsequence vs. substring
Not updating set/map properly

"""

"""
Problems involving arrays/strings with contiguous elements

When you need to find minimum/maximum/average of subarrays

When the problem involves finding subarrays/substrings that meet certain criteria

When a brute-force solution would have O(n²) or worse time complexity


Typically the time complexity is O(n)
"""

"""Leetcode 209     -- I did it myself"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """Original"""
        i = j = 0
        curr_sum = 0
        min_length = float('inf')

        while j <= len(nums) - 1:
            curr_sum += nums[j]
            while curr_sum >= target:
                min_length = min(min_length, j - i + 1)
                curr_sum -= nums[i]
                i += 1
            j += 1

    def minSubArrayLen_foorloop(self, target: int, nums: list[int]) -> int:
        """Original but using a for loop"""
        curr_sum = 0
        min_length = float('inf')
        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
