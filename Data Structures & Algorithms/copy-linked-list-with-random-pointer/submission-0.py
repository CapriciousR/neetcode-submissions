"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        og_dict = {}
        new_dict = {}

        curr = head
        dummy = Node(0)
        curn = dummy
        n = 0
        while curr:
            og_dict[curr] = n
            curn.next = Node(curr.val)
            curn = curn.next
            new_dict[n] = curn
            curr = curr.next
            n += 1
    
        
        curr = head
        curn = dummy.next

        while curr:
            if curr.random:
                curn.random = new_dict[og_dict[curr.random]]
            else:
                curn.random = None
            curn = curn.next
            curr = curr.next
        
        return dummy.next