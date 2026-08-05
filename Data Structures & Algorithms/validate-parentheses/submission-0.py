class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for char in s:
            if char in ["(","{","["]:
                stk.append(char)
            elif not stk:
                return False
            elif char == ")" and stk[-1] == "(":
                stk.pop()
            elif char == "}" and stk[-1] == "{":
                stk.pop()
            elif char == "]" and stk[-1] == "[":
                stk.pop()
            else:
                return False

        return True if not stk else False