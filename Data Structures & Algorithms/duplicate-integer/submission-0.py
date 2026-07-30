class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setA = set(nums)
        if len(setA) == len(nums):
            return False
        else:
            return True