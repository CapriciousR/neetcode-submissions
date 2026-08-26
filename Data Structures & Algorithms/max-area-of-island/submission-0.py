class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def areaIsland(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return 1 + areaIsland(r-1,c) + areaIsland(r+1,c) + areaIsland(r,c-1) + areaIsland(r,c+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    area = areaIsland(i,j)
                    max_area = max(area,max_area)
        
        return max_area
