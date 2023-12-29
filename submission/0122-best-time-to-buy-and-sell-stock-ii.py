class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0 # buy at index
        j = 0 # sell at index

        running_sum = 0
        maxx = 0
        while j < len(prices):
            if prices[j] - prices[i] > 0:
                maxx = prices[j] - prices[i]
                running_sum += maxx
                maxx = 0

            i = j
            j += 1

        return running_sum

