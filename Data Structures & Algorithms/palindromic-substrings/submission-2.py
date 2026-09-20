class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        res = 0

        def expandAroundCentre(i,j):
            nonlocal res

            while i>=0 and j<n and s[i]==s[j]:
                res += 1
                i-=1
                j+=1
            
        for i in range(n):
            expandAroundCentre(i,i)
            expandAroundCentre(i,i+1)
        
        return res


