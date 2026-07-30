class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dt = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dt:
                return [num_dt[diff],i]
            num_dt[nums[i]] = i