class Solution:
    def climbStairs(self, n: int) -> int:
        climb_ways = [0]*(n+1)
        climb_ways[0] = 1

        for i in range(n):
            if i+1 <= n:
                climb_ways[i+1] += climb_ways[i]
            if i+2 <= n:
                climb_ways[i+2] += climb_ways[i]
        
        return climb_ways[n]