# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = l = head

        while n > 0:
            r = r.next
            n-=1

        if not r:
            return head.next
        
        while r.next:
            r = r.next
            l = l.next
        
        nxt = l.next.next
        l.next = nxt
        
        return head