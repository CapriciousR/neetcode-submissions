class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = [0]*26

        for char in s1:
            s1_cnt[ord(char)-ord("a")] += 1

        s2_cnt = [0]*26

        for char in s2[:len(s1)]:
            s2_cnt[ord(char)-ord("a")] += 1
        
        if s1_cnt == s2_cnt:
            return True

        l = 0
        for r in range(len(s1),len(s2)):
            s2_cnt[ord(s2[r])-ord("a")] += 1
            s2_cnt[ord(s2[l])-ord("a")] -= 1
            l+=1

            print(s2_cnt)

            if s1_cnt == s2_cnt:
                return True
            
        return False
