class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
        majority = s[0]
        l=0
        longest = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            if freq[s[r]] > freq[majority]:
                majority = s[r]
            
            if (r-l+1-freq[majority]) > k:
                freq[s[l]] -= 1
                l+=1
            
            longest = max(longest,r-l+1)

        return longest
            
