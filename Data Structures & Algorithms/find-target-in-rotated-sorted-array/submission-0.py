class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m+1
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m
        
        return l if nums[l] == target else -1