# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx,val in enumerate(inorder)}
        self.pre_idx = 0
        def build(lbound, rbound):
            if lbound > rbound:
                return None
            
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            root_idx = inorder_map[root_val]
            root.left = build(lbound,root_idx-1)
            root.right = build(root_idx+1,rbound)

            return root
        
        return build(0,len(inorder)-1)