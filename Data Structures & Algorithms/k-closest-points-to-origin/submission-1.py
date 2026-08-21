class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for x,y in points:
            if len(heap) < k:
                heapq.heappush_max(heap,(x**2+y**2, (x,y)))
            else:
                heapq.heappushpop_max(heap,(x**2+y**2, (x,y)))
            
        return [point for distance, point in heap]
