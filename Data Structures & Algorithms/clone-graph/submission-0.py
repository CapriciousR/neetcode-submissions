"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_mapping = {}

        def cloneNodes(node):
            if node in node_mapping:
                return node_mapping[node]

            new_node = Node(node.val)
            node_mapping[node] = new_node

            for neighbor in node.neighbors:
                new_neighbor = cloneNodes(neighbor)
                new_node.neighbors.append(new_neighbor)
            
            return new_node
        
        return cloneNodes(node)