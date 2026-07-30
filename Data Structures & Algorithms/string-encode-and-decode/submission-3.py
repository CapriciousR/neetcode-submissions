class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st))
            res += "#"
            res += st
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        while i < len(s):
            res_st = ""
            start = i
            while i < len(s) and s[i] != "#":
                i += 1
            
            str_len = int(s[start:i])
            i += 1

            res.append(str(s[i:i+str_len]))
        
            i += str_len

        
        return res
