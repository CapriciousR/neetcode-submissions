class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
        max_freq = 0
        l=0
        longest = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq,freq[s[r]])
            
            if (r-l+1-max_freq) > k:
                freq[s[l]] -= 1
                l+=1
            
            longest = max(longest,r-l+1)

        return longest
            
