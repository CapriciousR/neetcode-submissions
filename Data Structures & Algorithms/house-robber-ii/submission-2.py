class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(start,end):
            prev1 = 0
            prev2 = 0

            for i in range(start,end):
                current = max(prev2+nums[i],prev1)
                prev2 = prev1
                prev1 = current
            
            return prev1
        
        with_last = rob_linear(1,len(nums))
        
        with_first = rob_linear(0,len(nums)-1)

        return max(with_last,with_first)