class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s):
            return s == s[::-1]
        
        res = []
        curr_parts = []

        def findPals(curr,i):
            if i >= len(s):
                if not curr:
                    res.append(curr_parts.copy())
                return
            
            curr += s[i]
            if isPal(curr):
                curr_parts.append(curr)
                findPals("",i+1)
                curr_parts.pop()
            
            findPals(curr,i+1)
        
        findPals("",0)
        return res