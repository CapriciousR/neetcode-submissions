class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr_parts = []

        def dfs(i):
            if i >= len(s):
                res.append(curr_parts.copy())
                return
            
            for j in range(i,len(s)):
                if isPal(s,i,j):
                    curr_parts.append(s[i:j+1])
                    dfs(j+1)
                    curr_parts.pop()

        def isPal(s,l,r):
            while l<=r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True
        
        dfs(0)
        return res