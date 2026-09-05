class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        prev3 = nums[0]
        prev2 = nums[1]
        prev1 = nums[0]+nums[2]

        for i in range(3,len(nums)):
            current = nums[i]+max(prev2,prev3)
            prev3 = prev2
            prev2 = prev1
            prev1 = current
        
        return max(prev1,prev2)