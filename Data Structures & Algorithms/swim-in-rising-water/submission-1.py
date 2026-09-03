class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        ROWS, COLS = len(grid), len(grid[0])

        queue = [(grid[0][0],(0,0))]

        visited = set()

        t = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while queue:
            ht, coords = heapq.heappop(queue)

            if coords in visited:
                continue

            r,c = coords

            visited.add((coords))
            t = max(t,ht)

            if (r,c) == (ROWS-1,COLS-1):
                return t

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited:
                    heapq.heappush(queue,(grid[nr][nc],(nr,nc)))
            

            


