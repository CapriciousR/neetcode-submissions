class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        dp = [float("inf")]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for denom in coins:
                if i-denom >=0:
                    dp[i] = min(dp[i],dp[i-denom]+1)
        
        return -1 if dp[amount] == float("inf") else dp[amount]