class Solution:

    def find_num_coins(self, coins, sub_amount):
        for coin in coins:
            if coin % sub_amount == 0:
                return coin/sub_amount
        return -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        # s_coins = set(coins)
        # if amount == 0:
        #     return 0

        # if amount < 0:
        #     return -1

        # dp = [-1] * (amount - 1)

        # dp[0] = self.find_num_coins(s_coins, 1)

        # for i in range(1, len(dp)):
            
        # print(dp)
        # return dp[-1][0]
        dp = [amount + 1] * (amount + 1)
    
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # Update dp for each coin denomination
        for coin in coins:
            for x in range(coin, amount + 1):
                # For each amount x, find the minimum number of coins needed
                # by considering the current coin
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1
