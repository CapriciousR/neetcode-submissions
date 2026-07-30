class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(list(s))
        sort_t = sorted(list(t))
        if sort_s == sort_t:
            return True
        else:
            return False