class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify_max(nums)

        for _ in range(k):
            num = heapq.heappop_max(nums)
        
        return num