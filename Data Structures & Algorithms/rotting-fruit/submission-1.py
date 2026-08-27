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
        
        if not freshf:
            return 0
        
        queue_len = len(queue)
        minute = 1

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            r,c = queue.popleft()
            queue_len -= 1

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    freshf -=1
                    queue.append((nr,nc))
                    if not freshf:
                        return minute
            
            if not queue_len:
                print(queue)
                minute += 1
                queue_len = len(queue)

        return minute if not freshf else -1

