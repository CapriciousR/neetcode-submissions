class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        import heapq
        heap = []
        for point in points:
            if len(heap) < k:
                heapq.heappush_max(heap,(math.sqrt(point[0]**2+point[1]**2),point))
            else:
                heapq.heappushpop_max(heap,(math.sqrt(point[0]**2+point[1]**2),point))
            
        return [point for distance, point in heap]
