class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def exploreIsland(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]=="0":
                return
            grid[r][c] = "0"
            exploreIsland(r+1,c)
            exploreIsland(r-1,c)
            exploreIsland(r,c+1)
            exploreIsland(r,c-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    exploreIsland(i,j)
                
        return res
