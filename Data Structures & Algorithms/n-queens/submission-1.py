class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return []

        res = []

        curr = []

        r = set()
        c = set()
        d1 = set()
        d2 = set()
        for i in range(n):
            r.add(i)
            c.add(i)
            d1.update([-i,i])
            d2.update([i,i+n-1])
        
        def solve(i):
            if i == n:
                res.append(curr.copy())
                return
            
            for j in range(n):
                if j in c and i-j in d1 and i+j in d2:
                    curr.append((i,j))
                    c.remove(j)
                    d1.remove(i-j)
                    d2.remove(i+j)
                    solve(i+1)
                    d2.add(i+j)
                    d1.add(i-j)
                    c.add(j)
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
                