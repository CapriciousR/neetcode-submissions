class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        subs = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
            
                if val == ".":
                    continue

                sub_key = (i//3,j//3)

                if val in rows[i] or val in cols[j] or val in subs[sub_key]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                subs[sub_key].add(val)

        return True