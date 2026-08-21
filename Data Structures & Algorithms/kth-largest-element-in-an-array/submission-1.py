class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums)-k

        def quickSelect(left,right):
            pivot = nums[right]

            p = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p]
            if p == target_idx:
                return nums[p]
            elif p < target_idx:
                return quickSelect(p+1,right)
            else:
                return quickSelect(left,p-1)
        
        return quickSelect(0,len(nums)-1)