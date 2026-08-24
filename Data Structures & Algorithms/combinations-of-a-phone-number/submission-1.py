class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []

        def backtrack(curr, i):
            if i >= len(digits):
                res.append(curr)
                return

            for char in digit_map[int(digits[i])]:
                backtrack(curr+char,i+1)
        
        backtrack("",0)

        return res

