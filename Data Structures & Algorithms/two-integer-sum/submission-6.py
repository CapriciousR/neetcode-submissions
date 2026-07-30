class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dt = {}

        for i in range(len(nums)):
            num_dt[nums[i]] = i
        
        for i in range(len(nums)):
            if target-nums[i] in num_dt and num_dt[target-nums[i]] != i:
                return [i,num_dt[target-nums[i]]]