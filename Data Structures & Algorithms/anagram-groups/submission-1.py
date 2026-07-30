class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        cntr = []

        for strr in strs:
            cnt = [0 for _ in range(26)]

            for char in strr:
                cnt[ord(char)-97] += 1
            
            if cnt in cntr:
                res[cntr.index(cnt)].append(strr)
            else:
                cntr.append(cnt)
                res.append([strr])
        
        return res
            
