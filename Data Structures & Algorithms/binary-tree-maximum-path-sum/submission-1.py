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

            left = findMaxPathSum(root.left)
            right = findMaxPathSum(root.right)

            max_at_curr_node = max(root.val, root.val+left+right)
            self.maxSum = max(self.maxSum, max_at_curr_node)
            return max(root.val, root.val+left, root.val+right, 0)
        
        findMaxPathSum(root)
        return self.maxSum