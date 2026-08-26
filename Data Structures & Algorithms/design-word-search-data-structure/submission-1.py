class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.is_end = True

    def search(self, word: str) -> bool:
        def searchWord(curr, i):
            if i == len(word):
                return curr.is_end
            if word[i] == ".":
                for key in curr.children:
                    if searchWord(curr.children[key],i+1):
                        return True
            elif word[i] in curr.children:
                if searchWord(curr.children[word[i]],i+1):
                    return True
            return False
        
        return searchWord(self.root,0)
                
                    
