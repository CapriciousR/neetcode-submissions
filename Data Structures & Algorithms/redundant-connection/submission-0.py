class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(n1):
            res = n1

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if p1 == p2:
                return False
            
            parent[p1] = p2
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        
