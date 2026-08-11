class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr1, arr2 = (nums1,nums2) if len(nums1) < len(nums2) else (nums2,nums1)

        half = (len(nums1)+len(nums2))//2
        l,r = 0,len(arr1)

        while l <= r:
            m = (l+r)//2
            n = half - m

            l1 = arr1[m-1] if m > 0 else float('-inf')
            l2 = arr2[n-1] if n > 0 else float('-inf')
            r1 = arr1[m] if m < len(arr1) else float('inf')
            r2 = arr2[n] if n < len(arr2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                return min(r1,r2) if (len(nums1)+len(nums2))%2 else (max(l1,l2)+min(r1,r2))/2

            elif l1 > r2:
                r = m-1
            else:
                l = m+1 