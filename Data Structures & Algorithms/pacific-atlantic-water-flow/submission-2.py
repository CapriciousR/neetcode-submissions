class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        
        pac_visited = set()
        atl_visited = set()

        def checkIsland(queue, ocean_set):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]

            while queue:
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr,c+dc

                    if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and heights[nr][nc]>=heights[r][c] and (nr,nc) not in ocean_set:
                        queue.append((nr,nc))
                        ocean_set.add((nr,nc))

        #check pacific tiles
        queue = deque()
        
        for i in range(len(heights)):
            queue.append((i,0))
            pac_visited.add((i,0))
        
        for i in range(1,len(heights[0])):
            queue.append((0,i))
            pac_visited.add((0,i))

        checkIsland(queue, pac_visited)

        l_row, l_col = len(heights)-1, len(heights[0])-1
        for i in range(len(heights)):
            queue.append((i,l_col))
            atl_visited.add((i,l_col))
        
        for i in range(len(heights[0])-1):
            queue.append((l_row,i))
            atl_visited.add((l_row,i))
            
        
        checkIsland(queue, atl_visited)

        return [list(coords) for coords in pac_visited&atl_visited]

         

        
        