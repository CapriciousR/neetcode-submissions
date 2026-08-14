# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(head):
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

        cnt = k-1

        dummy = ListNode(0,head)
        prev = dummy

        while head:
            if not cnt:
                nxt = head.next
                head.next = None
                sub_head = prev.next
                reverseList(sub_head)
                prev.next = head
                head = sub_head
                prev = head
                head.next = nxt
                
                cnt = k             
            else:
                head = head.next
                cnt -= 1
        
        return dummy.next

