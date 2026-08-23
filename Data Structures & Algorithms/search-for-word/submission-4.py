class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findWord(curr,i,j):
            if len(curr) == len(word):
                return True
            if i>=len(board) or j>=len(board[0]) or i < 0 or j < 0 or board[i][j] == -1:
                return False
            
            letter = board[i][j]
            letter_idx = len(curr)

            if letter == word[letter_idx]:
                curr += letter
                board[i][j] = -1
            
                if findWord(curr,i+1,j):
                    return True
                if findWord(curr,i,j+1):
                    return True
                if findWord(curr,i-1,j):
                    return True
                if findWord(curr,i,j-1):
                    return True
                
                board[i][j] = letter
            
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if findWord("",i,j):
                    return True
        
        return False
            
