# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        if not root:
            return False
        
        l = self.isSubtree(root.left, subRoot)
        if l: return True

        r = self.isSubtree(root.right, subRoot)
        if r: return True

        return isSameTree(root, subRoot)
        