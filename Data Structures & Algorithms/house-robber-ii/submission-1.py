class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1 = 0
        prev2 = 0

        for n in nums[1:]:
            current = max(prev2+n,prev1)
            prev2 = prev1
            prev1 = current
        
        with_last = prev1

        prev1 = 0
        prev2 = 0

        for n in nums[:len(nums)-1]:
            current = max(prev2+n,prev1)
            prev2 = prev1
            prev1 = current
        
        with_first = prev1

        return max(with_last,with_first)