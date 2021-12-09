'''
Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:
Input: n = 5
Output: 2
Explanation: 5 = 2 + 3

Example 2:
Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4

Example 3:
Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Constraints:
1 <= n <= 109
'''


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        upper_limit = ceil((2 * n + 0.25) ** 0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            n -= k
            if n % k == 0:
                count += 1
        return count