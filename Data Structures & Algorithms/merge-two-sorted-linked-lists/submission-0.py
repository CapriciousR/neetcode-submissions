# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        h1 = list1
        h2 = list2
        if h1.val < h2.val:
            h = h1
            h1 = h1.next
        else:
            h = h2
            h2 = h2.next
        new_head = h

        while h1 and h2:
            if h1.val < h2.val:
                h.next = h1
                h = h.next
                h1 = h1.next
            else:
                h.next = h2
                h = h.next
                h2 = h2.next
        
        if not h1:
            h.next = h2
        if not h2:
            h.next = h1

        return new_head
        