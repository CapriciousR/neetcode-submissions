class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token == "+":
                b = stk.pop()
                a = stk.pop()
                stk.append(a+b)
            elif token == "-":
                b = stk.pop()
                a = stk.pop()
                stk.append(a-b)
            elif token == "*":
                b = stk.pop()
                a = stk.pop()
                stk.append(a*b)
            elif token == "/":
                b = stk.pop()
                a = stk.pop()
                stk.append(int(a/b))
            else:
                stk.append(int(token))
        
        return stk[0]
            

            