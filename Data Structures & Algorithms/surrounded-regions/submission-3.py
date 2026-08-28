class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c]!="O":
                return
            
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        for i in range(ROWS):
            capture(i,0)
            capture(i,COLS-1)
        for i in range(COLS):
            capture(0,i)
            capture(ROWS-1,i)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
