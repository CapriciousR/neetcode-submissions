class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def genPar(curr,p):
            if len(curr) >= 2*n:
                res.append(curr)
                return
            
            if p < n:
                genPar(curr+"(",p+1)
            
            
            if len(curr) < 2*p:
                genPar(curr+")",p)
        
        genPar("",0)

        return res

            


