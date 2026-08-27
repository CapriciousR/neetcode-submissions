class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        INF = 2147483647

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            r,c = queue.popleft()
            val = grid[r][c]

            if r > 0 and grid[r-1][c] == INF:
                grid[r-1][c] = val+1
                queue.append((r-1,c))
            if r < len(grid)-1 and grid[r+1][c] == INF:
                grid[r+1][c] = val+1
                queue.append((r+1,c))
            if c > 0 and grid[r][c-1] == INF:
                grid[r][c-1] = val+1
                queue.append((r,c-1))
            if c < len(grid[0])-1 and grid[r][c+1] == INF:
                grid[r][c+1] = val+1
                queue.append((r,c+1))
            



        
        