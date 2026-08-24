class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {2:[chr(ord("a")+num) for num in range(3)],
        3:[chr(ord("a")+num) for num in range(3,6)],
        4:[chr(ord("a")+num) for num in range(6,9)],
        5:[chr(ord("a")+num) for num in range(9,12)],
        6:[chr(ord("a")+num) for num in range(12,15)],
        7:[chr(ord("a")+num) for num in range(15,19)],
        8:[chr(ord("a")+num) for num in range(19,22)],
        9:[chr(ord("a")+num) for num in range(22,26)]}

        def findCombs(i):
            if i == len(digits):
                return []
            if i == len(digits)-1:
                return digit_map[int(digits[i])]
            
            res = []
            for comb in findCombs(i+1):
                for char in digit_map[int(digits[i])]:
                    res.append(char+comb)
            
            return res
        
        return findCombs(0)