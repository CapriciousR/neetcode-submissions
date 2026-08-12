# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        prev = None
        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt
        l2 = prev

        l1 = head
        print(l1.val)

        while l2:
            nxt1, nxt2 = l1.next, l2.next

            l1.next = l2
            l2.next = nxt1

            l1, l2 = nxt1, nxt2
        


