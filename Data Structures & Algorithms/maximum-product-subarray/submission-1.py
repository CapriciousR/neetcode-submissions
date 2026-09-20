class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = float("inf")
        max_prod = float("-inf")

        res = float("-inf")

        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res,max_prod)

            if nums[i] < 0:
                res = max(res,max_prod)
                min_prod, max_prod = max_prod, min_prod
            
            min_prod = min(nums[i],min_prod*nums[i])
            max_prod = max(nums[i],max_prod*nums[i])
        
        res = max(res,max_prod)
        
        return res
                
            
