class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def findCombs(total, i):
            if i >= len(nums):
                return
            
            if total >= target:
                if total == target:
                    res.append(curr.copy())
                return

            curr.append(nums[i])
            total += nums[i]

            findCombs(total, i)

            curr.pop()
            total -= nums[i]
            
            findCombs(total, i+1)
        
        findCombs(0,0)

        return res
