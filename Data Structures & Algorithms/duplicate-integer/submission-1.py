from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = defaultdict(int)
        for num in nums:
            if num in nums_seen:
                return True
            else:
                nums_seen[num] += 1
        
        return False