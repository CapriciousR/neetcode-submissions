class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(c.lower() for c in s if c.isalnum())
        
        return True if clean_s == clean_s[::-1] else False