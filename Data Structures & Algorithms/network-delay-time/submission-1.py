class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        adj = {i+1:[] for i in range(n)}

        for src,des,time in times:
            adj[src].append((des,time))
        
        visited = set()
        queue = [(0,k)]


        while queue and len(visited)<n:
            time, node = heapq.heappop(queue)

            if node in visited:
                continue
                
            visited.add(node)

            for neighbor,etime in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (time+etime,neighbor))
            
        return time if len(visited) == n else -1


        
        