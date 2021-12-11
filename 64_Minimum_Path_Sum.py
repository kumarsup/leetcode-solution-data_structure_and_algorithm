'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the
sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        #         def calculate(i, j):
        #             if i == M or j == N: return float('inf')
        #             if i == M-1 and j == N-1: return grid[i][j]
        #             return grid[i][j] + min(calculate(i+1, j), calculate(i, j+1))

        #         return calculate(0, 0)

        # dp = [[0 for i in range(N)] for j in range(M)]

        for i in range(M):
            for j in range(N):
                val = 0
                if i > 0 and j > 0:
                    val = min(grid[i][j - 1], grid[i - 1][j])
                elif i > 0:
                    val = grid[i - 1][j]
                elif j > 0:
                    val = grid[i][j - 1]
                grid[i][j] = val + grid[i][j]
        return grid[M - 1][N - 1]