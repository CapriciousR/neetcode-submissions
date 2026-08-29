class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(node: int) -> int:
            """
            Finds the root parent of a node with path compression.

            Args:
                node: The node to find the root parent for

            Returns:
                The root parent of the node
            """
            if parent[node] != node:
                # Path compression: directly connect node to root
                parent[node] = find(parent[node])
            return parent[node]

        # Initialize parent array where each node is its own parent
        parent = list(range(n))

        # Track number of connected components (initially n separate nodes)
        num_components = n

        # Process each edge
        for node_a, node_b in edges:
            # Find root parents of both nodes
            root_a = find(node_a)
            root_b = find(node_b)

            # If both nodes already have the same root, adding this edge creates a cycle
            if root_a == root_b:
                return False

            # Union: connect the two components by making one root the parent of the other
            parent[root_a] = root_b

            # Decrease component count as two components are merged
            num_components -= 1

        # A tree must have exactly one connected component
        return num_components == 1