"""
Heap is a data structure that goes first in last out
We can use the builtin heap package called heapq to do this
"""

import heapq


class Example:
    """Consider this example form leetcode 703"""
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # Convert nums into a heap
        # If the heap is larger than k,
        # remove the smallest elements until it has exactly k elements
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)  # Pops from the top because first in last out

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)  # heapq will push it to where it belongs
        # if after adding the new value, the heap has more than k elements, pop the smallest
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # The smallest element in the heap is now the k-th largest element
        # This is because heappop from the top instead from the end
        return self.nums[0]
