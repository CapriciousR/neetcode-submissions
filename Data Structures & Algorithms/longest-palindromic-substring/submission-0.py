class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = (0,0)

        def checkPals(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            
            return l+1,r-1


        for i in range(len(s)):
            l,r = checkPals(i,i)

            if res[0] < r-l+1:
                res = (r-l+1,l)

            if i+1<len(s) and s[i+1]==s[i]:
                l,r = checkPals(i,i+1)

                if res[0] < r-l+1:
                    res = (r-l+1,l)
            
            print(res)
        
        return s[res[1]:res[1]+res[0]]
