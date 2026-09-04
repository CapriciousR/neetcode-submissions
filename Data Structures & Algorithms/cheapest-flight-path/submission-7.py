class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import deque

        adj = {i:[] for i in range(n)}

        for source,dest,price in flights:
            adj[source].append((dest,price))
        
        queue = deque([(0,src)])
        stops = 0
        prices = [float("inf")]*n

        while queue and stops<=k:
            for _ in range(len(queue)):
                cost,airport = queue.popleft()

                for nairport,ncost in adj[airport]:
                    if cost+ncost < prices[nairport]:
                        prices[nairport] = cost+ncost
                        queue.append((cost+ncost,nairport))
            stops+=1
        
        return prices[dst] if prices[dst] != float("inf") else -1
            
