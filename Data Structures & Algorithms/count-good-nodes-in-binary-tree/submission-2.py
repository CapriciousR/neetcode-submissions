# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def findGoodNodes(root, max_so_far):
            if not root:
                return 0
            is_good = 1 if root.val >= max_so_far else 0
            max_so_far = max(root.val, max_so_far)
            
            return is_good+findGoodNodes(root.left, max_so_far)+findGoodNodes(root.right, max_so_far)
            
        
        return findGoodNodes(root, root.val)

