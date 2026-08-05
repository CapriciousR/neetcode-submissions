class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = ""
        t_cnt = {}

        cnt = len(t)

        for char in t:
            if char in t_cnt:
                t_cnt[char] += 1
            else:
                t_cnt[char] = 1

        l = 0
        
        for r in range(len(s)):
            if s[r] in t_cnt:
                t_cnt[s[r]] -= 1

                if t_cnt[s[r]] >= 0:
                    cnt -= 1

                while cnt == 0:
                    if res == "" or len(res) > r-l+1:
                        res = s[l:r+1]
                    if s[l] in t_cnt:
                        t_cnt[s[l]] += 1
                        if t_cnt[s[l]] > 0:
                            cnt += 1
                    l += 1
        
        return res

