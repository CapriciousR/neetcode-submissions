class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)

        for strr in strs:
            cnt = [0 for _ in range(26)]

            for char in strr:
                cnt[ord(char)-ord("a")] += 1
            
            res[tuple(cnt)].append(strr)
        
        return list(res.values())
            
