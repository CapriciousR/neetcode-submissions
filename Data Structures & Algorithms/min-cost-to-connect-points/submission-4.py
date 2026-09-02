class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq

        n = len(points)
        queue = [(0,0)]
        visited = set()
        total = 0

        while len(visited) < n:
            cost,pt_idx = heapq.heappop(queue)

            if pt_idx in visited:
                continue
            
            visited.add(pt_idx)
            total += cost

            x1,y1 = points[pt_idx]
            
            for next_idx in range(n):
                if next_idx not in visited:
                    x2,y2 = points[next_idx]
                    heapq.heappush(queue,(abs(x1-x2)+abs(y1-y2),next_idx))
            
        return total
        
        
            