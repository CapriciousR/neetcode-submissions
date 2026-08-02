class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = []
        r_max = []

        highest = 0
        for ht in height:
            l_max.append(highest)

            highest = max(highest,ht)
        
        highest = 0
        for ht in height[::-1]:
            r_max.append(highest)

            highest = max(highest,ht)
        
        r_max.reverse()
        
        total = 0
        for i in range(len(height)):
            stored = min(l_max[i],r_max[i])-height[i]
            print(stored,i)

            total += stored if stored > 0 else 0
        
        return total