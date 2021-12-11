'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prof = [0] * (n + 2)
        i = n - 1

        while i >= 0:
            j = i + 1
            while j < n:
                prof[i] = max(prof[i], prices[j] - prices[i] + prof[j + 2])
                j += 1
            prof[i] = max(prof[i], prof[i + 1])
            i -= 1
        return prof[0]