class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return []

        res = []
        curr = []

        c = set()
        d1 = set()
        d2 = set()
        
        def solve(i):
            if i == n:
                res.append(curr.copy())
                return
            
            for j in range(n):
                if j not in c and i-j not in d1 and i+j not in d2:
                    curr.append((i,j))
                    c.add(j)
                    d1.add(i-j)
                    d2.add(i+j)
                    
                    solve(i+1)
                    
                    c.remove(j)
                    d1.remove(i-j)
                    d2.remove(i+j)
                    
                    curr.pop()
            
        solve(0)
        
        ans = []

        for sol in res:
            solu = []
            for i,j in sol:
                row_str = "." * j + "Q" + "." * (n - j - 1)
                solu.append(row_str)
            ans.append(solu)


        return ans
                