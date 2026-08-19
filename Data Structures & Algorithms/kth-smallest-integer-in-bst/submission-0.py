# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def findkth(root, k):
            if not root:
                return (None, k)
            
            left, k = findkth(root.left, k)
            if not k:
                return (left, 0)

            k -= 1
            if not k:
                return (root, k)

            right, k = findkth(root.right, k)
            if not k:
                return (right, 0)
            
            return (None, k)
        
        return findkth(root, k)[0].val