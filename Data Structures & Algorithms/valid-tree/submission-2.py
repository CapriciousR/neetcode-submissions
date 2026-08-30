class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        parent = [i for i in range(n)]

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
                return False
        
        return True
    

