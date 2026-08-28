class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        adj_map = {i:[] for i in range(numCourses)}
        inorder = [0]*numCourses
        res = []

        for crs,pre in prerequisites:
            adj_map[pre].append(crs)
            inorder[crs] += 1
        
        queue = deque()

        for crs in range(numCourses):
            if inorder[crs] == 0:
                queue.append(crs)
            
        while queue:
            crs = queue.popleft()
            res.append(crs)

            for adj in adj_map[crs]:
                inorder[adj] -= 1
                if inorder[adj] == 0:
                    queue.append(adj)
        
        return res if len(res) == numCourses else []

        