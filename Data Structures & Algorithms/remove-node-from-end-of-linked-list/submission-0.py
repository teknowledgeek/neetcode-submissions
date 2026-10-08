# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first = head

        for _ in range(n):
            first = first.next

        dummy = ListNode(-1)

        second = dummy
        second.next = head

        
        while first :

            first = first.next
            second = second.next

        # print(second.val)
        temp = second.next.next
        second.next = temp

        while second:
            second = second.next


        return dummy.next