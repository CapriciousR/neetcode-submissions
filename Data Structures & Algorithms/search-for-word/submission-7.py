class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, idx):
            # Base Case 1: We found all letters
            if idx == len(word):
                return True
            
            # Base Case 2: Out of bounds, visited, or wrong letter
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[idx] or board[r][c] == "-1"):
                return False
            
            temp = board[r][c]
            board[r][c] = "-1"
            
            res = (dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1))
            
            board[r][c] = temp
            
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                    
        return False
        
