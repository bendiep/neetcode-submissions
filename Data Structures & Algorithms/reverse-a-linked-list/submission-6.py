# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 'previous' will point to the head of the reversed list
        previous = None

        # Start at the head of the original list
        current = head

        # Keep looping until we reach the end of the list
        while current:

            # Save the next node before we change any pointers
            next = current.next

            # Reverse this node's pointer
            # (instead of pointing forward, point it backward)
            current.next = previous

            # Move 'previous' forward to this node
            # (this node is now the new head of the reversed part)
            previous = current

            # Move to the next node in the original list
            current = next

        # At the end, 'previous' is the new head of the reversed list
        return previous
