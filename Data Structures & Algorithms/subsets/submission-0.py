class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def findSubsets(curr,i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])  
            findSubsets(curr,i+1)

            curr.pop()
            findSubsets(curr,i+1)
        
        findSubsets([],0)

        return res