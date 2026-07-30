class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.lower()
        t.lower()
        s_cnt = [0 for _ in range(26)]
        t_cnt = [0 for _ in range(26)]

        for char in s:
            s_cnt[ord(char)-97] += 1
        
        for char in t:
            t_cnt[ord(char)-97] += 1

        if s_cnt == t_cnt:
            return True
        else:
            return False
            
