class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        roots = {i:1 for i in range(n)}

        def find(n1):
            res = n1

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res

        def union(n1,n2):
            # print(n1,n2)
            p1,p2 = find(n1),find(n2)
            # print(p1,p2)
            # print(roots)

            if p1 == p2:
                return

            if roots[p1] > roots[p2]:
                parent[p2] = p1
                roots[p1] += roots[p2]
                del roots[p2]
            
            else:
                parent[p1] = p2
                roots[p2] += roots[p1]
                del roots[p1]
        
        for n1,n2 in edges:
            union(n1,n2)
            
        return len(roots)

