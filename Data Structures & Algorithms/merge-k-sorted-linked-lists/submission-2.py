# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        def mergeLists(list1, list2):
            dummy = ListNode(0)
            curr = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            # Pulled outside the loop
            curr.next = list1 if list1 else list2
            
            return dummy.next
        
        interval = 1
        amount = len(lists)
        
        # O(1) space in-place manipulation
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = mergeLists(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0]
