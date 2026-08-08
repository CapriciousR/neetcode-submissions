class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best = r = max(piles) 
        l = 1

        while l <= r:
            m = (l+r)//2
            print(m)
            tt = sum([-(p//-m) for p in piles])

            if tt > h:
                l = m+1
            else:
                best = min(best,m)
                r = m-1
        
        return best