class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = 0
        sell = 1
        maxx = 0
        while sell < len(prices):
            if prices[sell] <= prices[buy]:
                buy = sell
                sell += 1
            else:
                proposed_profit = prices[sell] - prices[buy]
                maxx = max(proposed_profit, maxx)
                sell += 1

        return maxx
