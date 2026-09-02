class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq

        queue = []
        visited = set()
        
        def addPaths(point):
            for npoint in points:
                if npoint != point and tuple(npoint) not in visited:
                    x1,y1 = point
                    x2,y2 = npoint
                    heapq.heappush(queue,(abs(x1-x2)+abs(y1-y2),(x1,y1),(x2,y2)))

        addPaths(points[0])
        total = 0
        visited.add(tuple(points[0]))

        while queue and len(visited) < len(points):
            cost,p1,p2 = heapq.heappop(queue) 

            if p1 and p2 in visited:
                continue
            
            elif p1 in visited:
                addPaths(p2)
                visited.add(p2)

            else:
                addPaths(p1)
                visited.add(p1)
            
            total += cost
        
        return total
            



            

