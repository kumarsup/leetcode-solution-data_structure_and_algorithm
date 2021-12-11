'''
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        numbers = set()
        for i in range(2, int(sqrt(n)) + 1):
            if i not in numbers:
                for j in range(i * i, n, i):
                    numbers.add(j)
        return n - len(numbers) - 2