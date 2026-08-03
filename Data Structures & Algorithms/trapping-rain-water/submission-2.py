class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1

        l_max = height[l]
        r_max = height[r]

        tot = 0

        while l <= r:
            if l_max < r_max:
                stored = min(l_max,r_max)-height[l]
                print(l,stored)
                tot += stored if stored > 0 else 0
                l_max = max(l_max,height[l])
                l+=1

            else:
                stored = min(l_max,r_max)-height[r]
                print(r,stored)
                tot += stored if stored > 0 else 0
                r_max = max(r_max,height[r])
                r-=1
        
        return tot

        