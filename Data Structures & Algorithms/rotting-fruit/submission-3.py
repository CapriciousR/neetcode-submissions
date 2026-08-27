class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        queue = deque()
        freshf = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    freshf += 1
        
        time = 0

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue and freshf:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr,c+dc

                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshf -=1
                        queue.append((nr,nc))
            
            time += 1

        return time if not freshf else -1

