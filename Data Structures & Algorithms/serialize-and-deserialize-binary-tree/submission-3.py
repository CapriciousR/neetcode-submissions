# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        def dfs(node):
            if not node:
                data.append("N")
                return
            data.append(str(node.val))
            
            dfs(node.left)
            dfs(node.right)

            return
        
        dfs(root)

        return ("#".join(data))

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = iter(data.split('#'))

        def build():
            val = next(data)
            if val == "N":
                return None
            
            root = TreeNode(int(val))

            root.left = build()
            root.right = build()

            return root
        
        return build()