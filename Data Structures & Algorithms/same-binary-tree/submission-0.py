# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTrees(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (root1 and not root2):
                return False
            if root1.val != root2.val:
                return False
            
            l_res = checkTrees(root1.left, root2.left)
            r_res = checkTrees(root1.right, root2.right)

            return l_res and r_res
    
        return checkTrees(p, q)