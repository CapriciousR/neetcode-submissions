class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        INF = 2147483647

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.popleft()
            val = grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == INF:
                    grid[nr][nc] = val + 1
                    queue.append((nr, nc))
            



        
        