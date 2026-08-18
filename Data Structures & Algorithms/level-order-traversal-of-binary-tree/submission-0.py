# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = [[root.val]] if root else []

        queue = deque([root])
        level_length = len(queue)

        while queue:
            if not level_length:
                res.append([node.val for node in queue])
                level_length = len(queue)

            node = queue.popleft()
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_length -= 1

            
        
        return res