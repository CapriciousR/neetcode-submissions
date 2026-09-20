class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]

        res = nums[0]

        for n in nums[1:]:
            tmp_min = curr_min * n
            tmp_max = curr_max * n

            curr_max = max(n,tmp_min,tmp_max)
            curr_min = min(n,tmp_min,tmp_max)

            res = max(res, curr_max)
        
        return res
                
            
