"""Linked list"""
"""
Over time that I've been doing different questions, I've realized how to deal with linked lists
You really can't do much with them but however, you can put them into a temporary list 
and then put them back into a linked list later!
"""

"""
This process include the usage of using a dummy node, and a current.
Use the example of sorting a linked list. 
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Original Solution"""

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []  # put all the values into a list
        while head:
            temp.append(head.val)
            head = head.next

        dummy = ListNode(0)  # The dummy node
        current = dummy  # The current
        temp.sort()  # Sort them as a list

        for i in temp:
            current.next = ListNode(i)  # put them back in to linked list
            current = current.next  # next element
        return dummy.next  # dummy is = ListNode(0) as we defined before, dummy.next is the real linked list


"""Now this is how to directly sort a linked list is to use merge sort"""
"""Be aware that this is actually slower than converting"""
"""
Time complexity: O(n log n)  # Standard merge sort time
Space complexity: O(log n)
"""


class SortLinkedList:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.find_middle(head)
        left = head  # head to mid
        right = mid.next  # mid to end
        mid.next = None  # Break the link

        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        return self.merge_sort(left_sorted, right_sorted)

    def find_middle(self, head):  # How to find the middle node in linked lists
        """When fast is two times faster than slow, when fast reaches its end,
        slow would be at in the exact middle"""
        slow = head
        fast = head.next  # Only works if fast starts at head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(self, left, right):
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        current.next = left if left else right  # remaining elements
        return dummy.next


"""This is extremely cool, as I'm learning how to do this, I'm getting better with linked lists"""
"""We need to practice more with this"""


"""Take this example about deleting nodes from linked list"""
"""Leetcode #19"""


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    temp = []
    while head:
        temp.append(head.val)
        head = head.next

    length = len(temp)
    dummy = ListNode(0)
    current = dummy

    for i in range(length):
        if i is not length - n:
            current.next = ListNode(temp[i])
            current = current.next
    return dummy.next
