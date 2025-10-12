"""Three ways of finding duplicates in a list"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """Original"""
        seen = {}
        for i in nums:
            if i in seen:
                return i
            seen[i] = 1


# Speed: O(n)
# Space: O(n)


class Solution1:
    def findDuplicate(self, nums: list[int]) -> int:
        """Original, in-place marking"""
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            else:
                nums[index] = -nums[index]


# Speed: O(n)
# Space: O(1)


class Solution2:
    def findDuplicate(self, nums: list[int]) -> int:
        """Really cool, but not original"""
        begin, end = 1, len(nums) - 1
        while begin < end:
            mid = int((begin + end) // 2)

            count = sum(i <= mid for i in nums)

            if count > mid:
                end = mid
            else:
                begin = mid + 1

        return begin


# Speed: O(n log n)
# Space: O(1)


"""Using two pointers, fast and slow"""


def findDuplicate(nums):
    # Phase 1: detect cycle
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: find entrance to cycle (duplicate number)
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


# speed: O(n)
# space: O(1)
