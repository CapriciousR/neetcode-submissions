class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        self.root = TrieNode()

        def addWord(word):
            curr = self.root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            
            curr.is_end = True
            curr.word = word

        for word in words:
            addWord(word)
        
        def searchWords(r,c,curr):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == -1:
                return
            letter = board[r][c]
            if letter in curr.children:
                next_node = curr.children[letter]
                if next_node.is_end:
                    res.append(next_node.word)
                    next_node.is_end = False
                
                board[r][c] = -1
                searchWords(r+1,c,next_node)
                searchWords(r-1,c,next_node)
                searchWords(r,c+1,next_node)
                searchWords(r,c-1,next_node)
                board[r][c] = letter

                if not next_node.children and not next_node.is_end:
                    del curr.children[letter]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                searchWords(i,j,self.root)
        
        return res



