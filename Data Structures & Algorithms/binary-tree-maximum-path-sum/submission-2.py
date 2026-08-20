# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        def findMaxPathSum(root):
            if not root:
                return 0

            left = max(findMaxPathSum(root.left),0)
            right = max(findMaxPathSum(root.right),0)

            self.maxSum = max(self.maxSum, root.val+left+right)
            return root.val + max(left,right)
        
        findMaxPathSum(root)
        return self.maxSum