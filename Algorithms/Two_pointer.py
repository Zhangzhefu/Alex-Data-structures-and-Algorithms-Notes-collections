"""
You use two pointers that move through the structure — either from the same direction, opposite directions, or with different speeds.

The goal is often to compare elements, find a condition, or reduce time complexity (often from
O(n^2) to O(n).


"""


def is_subsequence(s1, s2):
    """Same direction: i and j both move forward"""
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)


def two_sum_sorted(arr, target):
    """Opposite direction: left starts at 0 and right starts at the end, moves inward"""
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False


def has_cycle(head):
    """Different speeds: slow moves 1 and fast moves 2, detect cycles"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def linkedlist_find_mid(head):
    """Fast travel twice as fast as slow, when fast reaches the end, slow is at mid-point"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def inplace_remove_element(nums: list[int], target: int) -> int:
    """receive list of numbers, we need to remove numbers in-place with O(1) extra memory"""
    j = 0
    for i in range(len(nums)):
        if nums[i] != target:
            nums[j] = nums[i]
            j += 1
    return j
    # This is just a place-holder, the most important part is in-place removing the element in the list


def removeDuplicates(self, nums: list[int]) -> int:
    """A transformation of the previous"""
    if len(nums) <= 2:
        return len(nums)  # The first two elements are always okay

    pos = 2  # We start at 2, this is the writing slot

    for i in range(2, len(nums)):
        if nums[i] != nums[pos - 2]:
            # if 2 before the current is the same as current,
            # the current the third duplicate, which means we simply do nothing
            nums[pos] = nums[i]  # If not, slide the current value into the pos slot
            pos += 1  # After this operation increase pos by 1

    return pos
