class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}

        def dp(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            min_count = float('inf')
            for coin in coins:
                res = dp(rem - coin)
                if res != -1:
                    min_count = min(min_count, res + 1)

            memo[rem] = -1 if min_count == float('inf') else min_count
            return memo[rem]

        return dp(amount)