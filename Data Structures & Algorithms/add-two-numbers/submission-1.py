# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = 0

        face_val = 1
        while l1:
            num1 += l1.val*face_val
            l1 = l1.next
            face_val *= 10
        
        num2 = 0

        face_val = 1
        while l2:
            num2 += l2.val*face_val
            l2 = l2.next
            face_val *= 10

        res = num1 + num2
        dummy = ListNode(0)
        curr = dummy

        while res:
            curr.next = ListNode(res%10)
            res = res//10
            curr = curr.next
        
        return dummy.next if dummy.next else ListNode(0)
