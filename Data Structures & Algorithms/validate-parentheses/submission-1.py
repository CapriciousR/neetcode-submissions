class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        brac = {")":"(","}":"{","]":"["}

        for char in s:
            if char in brac:
                if not stk or stk[-1] != brac[char]:
                    return False
                stk.pop()
            else:
                stk.append(char)
        
        return not stk