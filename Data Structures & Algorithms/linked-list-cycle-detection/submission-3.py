# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        if not head.next:
            return False

        if head and head.next:

            slow = head
            fast = head

            current = head

            while slow and fast:
                slow = slow.next

                fast = fast.next.next if fast.next else None

                if slow == fast:
                    return True
            

        return False 