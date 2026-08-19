# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def findGoodNodes(root, max_so_far):
            nonlocal res
            if not root:
                return
            if root.val >= max_so_far:
                max_so_far = root.val
                res += 1
            
            findGoodNodes(root.left, max_so_far)
            findGoodNodes(root.right, max_so_far)
        
        res = 0
        findGoodNodes(root, root.val)

        return res