class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        
        freq = defaultdict(int)
        l,r = 0,0

        longest = 0
        cnt = 0

        while r<len(s):
            freq[s[r]]+=1

            if freq[s[r]] > 1:
                longest = max(longest,cnt)
                while freq[s[r]] > 1:
                    cnt-=1
                    freq[s[l]] -= 1
                    l+=1
                
            cnt += 1
            r+=1
        
        longest = max(longest,cnt)

        return longest