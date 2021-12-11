'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6


Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        M, N = m, n

        #         def calculate(i, j):
        #             if i == M or j == N: return float('inf')
        #             if i == M-1 and j == N-1: return grid[i][j]
        #             return grid[i][j] + min(calculate(i+1, j), calculate(i, j+1))

        #         return calculate(0, 0)

        grid = [[0 for i in range(N)] for j in range(M)]
        for i in range(M):
            for j in range(N):
                val = 0
                if i > 0 and j > 0:
                    val = grid[i][j - 1] + grid[i - 1][j]
                else:
                    val = 1
                grid[i][j] = val
        return grid[M - 1][N - 1]