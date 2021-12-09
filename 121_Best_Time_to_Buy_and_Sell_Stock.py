class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, prices[0]
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            profit = max(profit, prices[i] - buy)
        return profit