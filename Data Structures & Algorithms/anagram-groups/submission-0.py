class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = [[strs[0]]]
        if len(strs) == 1:
            return result
        for i in range(1, len(strs)):
            foundGrp = False
            for group in result:
                if Counter(strs[i]) == Counter(group[0]):
                    group.append(strs[i])
                    foundGrp = True
                    break
            if foundGrp == False:
                result.append([strs[i]])
        
        return result
            
            