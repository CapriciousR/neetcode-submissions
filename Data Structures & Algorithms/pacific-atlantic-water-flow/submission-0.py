class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        island = [[0 for i in range(len(heights[0]))] for j in range(len(heights))]

        res = [] 

        def checkIsland(queue):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            visited = {x for x in queue}

            print(visited)

            while queue:
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr,c+dc

                    if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and heights[nr][nc]>=heights[r][c] and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        if island[nr][nc] == 0:
                            island[nr][nc] = 1
                        elif island[nr][nc] == 1:
                            island[nr][nc] = 2
                            res.append([nr,nc])

        #check pacific tiles
        queue = deque()
        
        for i in range(len(heights)):
            queue.append((i,0))
            island[i][0] = 1
        
        for i in range(1,len(heights[0])):
            queue.append((0,i))
            island[0][i] = 1

        checkIsland(queue)

        print(island)

        l_row, l_col = len(heights)-1, len(heights[0])-1
        for i in range(len(heights)):
            queue.append((i,l_col))
            if island[i][l_col]==1:
                island[i][l_col] = 2
                res.append([i,l_col])
            else:
                island[i][l_col] = 1
        
        for i in range(len(heights[0])-1):
            queue.append((l_row,i))
            if island[l_row][i]==1:
                island[l_row][i] = 2
                res.append([l_row,i])
            else:
                island[l_row][i] = 1
            
        
        checkIsland(queue)

        print(island)

        return res

         

        
        