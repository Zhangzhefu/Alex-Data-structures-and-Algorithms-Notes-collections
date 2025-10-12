class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def turtle_hare(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


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


"""Sure! Floyd’s Cycle Detection Algorithm — also known as the Tortoise and Hare algorithm — is a clever way to 
detect cycles in a linked list (or any iterable structure with nodes and pointers) using two pointers moving at 
different speeds.

If there's no cycle, the faster pointer will eventually reach the end (null).
If there's a cycle, the faster pointer will eventually "lap" the slower one and they will meet.


Initialize two pointers:

slow (the tortoise): moves 1 step at a time.

fast (the hare): moves 2 steps at a time.

Traverse the list:

If at any point slow == fast, a cycle exists.

If fast or fast.next becomes null, the list ends — so no cycle.

Time: O(n) — each pointer moves at most n times before meeting or reaching the end.

Space: O(1) — no extra memory used.
"""
