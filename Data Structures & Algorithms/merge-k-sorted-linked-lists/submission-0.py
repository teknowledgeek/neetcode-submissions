# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1 :

            mergedList = []

            for i in range(0, len(lists), 2):
                # print(i)
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None

                mergedList.append(self.mergeLists(list1, list2))
                # print(mergedList[0].val)

            lists = mergedList

        return lists[0]

    def mergeLists(self, list1: ListNode, list2: ListNode ) -> Optional[ListNode]:
        dummy = ListNode(-1)

        current = dummy

        while list1 and list2 :

            if list1.val < list2.val:

                current.next = list1
                current = current.next
                list1 = list1.next

            else:
                current.next = list2
                current = current.next
                list2 = list2.next

        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return dummy.next