class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for n in nums:
            current = max(n+prev2,prev1)
            prev2 = prev1
            prev1 = current
        
        return prev1