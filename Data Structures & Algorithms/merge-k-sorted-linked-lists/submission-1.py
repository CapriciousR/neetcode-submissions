# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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

                curr.next = list1 if list1 else list2
            
            return dummy.next
        
        if not lists:
            return None
        
        curr_lists = lists

        while len(curr_lists) > 1:
            new_lists = []
            for i in range(1,len(curr_lists),2):
                new_lists.append(mergeLists(curr_lists[i-1],curr_lists[i]))
            
            if len(curr_lists) % 2:
                new_lists.append(curr_lists[-1])
            curr_lists = new_lists
        
        return curr_lists[0]
