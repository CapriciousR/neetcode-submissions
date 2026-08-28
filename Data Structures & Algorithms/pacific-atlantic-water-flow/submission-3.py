class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque

        ROW, COL = len(heights), len(heights[0])
        
        pac = set()
        atl = set()

        def dfs(r,c,visited,prevHt):
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r,c) in visited or heights[r][c] < prevHt:
                return

            visited.add((r,c))

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])

        for i in range(COL):
            dfs(0,i,pac,float("-inf"))
            dfs(ROW-1,i,atl,float("-inf"))

        for i in range(ROW):
            dfs(i,0,pac,float("-inf"))
            dfs(i,COL-1,atl,float("-inf"))

        return [list(coords) for coords in pac & atl]

         

        
        