class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        res = []

        queue = deque()

        maxi = float("-inf")
        for num in nums[:k]:
            while queue and num > queue[-1]:
                queue.pop()
            queue.append(num)
        
        res.append(queue[0])

        for r in range(k,len(nums)):
            if queue[0] == nums[r-k]:
                queue.popleft()
            while queue and nums[r] > queue[-1]:
                queue.pop()
            queue.append(nums[r])
            res.append(queue[0])
        
        return res
