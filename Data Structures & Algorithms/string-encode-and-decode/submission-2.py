class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += word+"."
        return result 

    def decode(self, s: str) -> List[str]:
        result_list = []
        word = ""
        for char in s:
            if char == ".":
                result_list.append(word)
                word = ""
            else:
                word += char

        return result_list