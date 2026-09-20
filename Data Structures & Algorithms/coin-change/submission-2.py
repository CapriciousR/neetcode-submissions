class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        dp = [float("inf")]*(amount+1)
        dp[0] = 0

        for i in range(amount):
            if dp[i] == float("inf"):
                continue
            for denom in coins:
                if i+denom <= amount:
                    dp[i+denom] = min(dp[i]+1,dp[i+denom])
        
        return -1 if dp[amount] == float("inf") else dp[amount]