class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
        
            for num in nums:
                if num in curr:
                    continue
                
                curr.append(num)
                dfs()

                curr.pop()
        
        dfs()

        return res