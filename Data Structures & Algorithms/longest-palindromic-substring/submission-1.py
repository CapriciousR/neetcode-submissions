class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = (0,0)

        def checkPals(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            
            return l+1,r-1


        for i in range(len(s)):
            l1,r1 = checkPals(i,i)

            if res[0] < r1-l1+1:
                res = (r1-l1+1,l1)

            l2,r2 = checkPals(i,i+1)

            if res[0] < r2-l2+1:
                res = (r2-l2+1,l2)
            
        
        return s[res[1]:res[1]+res[0]]
