'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move
outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res, M, N = 0, len(matrix), len(matrix[0])

        dp = [[0] * N for i in range(M)]

        def backTrack(i=0, j=0):
            nonlocal M, N, res, dp
            ans = 0
            if dp[i][j] != 0: return dp[i][j]

            for move in moves:
                x = i + move[0]
                y = j + move[1]
                if x >= M or y >= N or x < 0 or y < 0: continue
                if matrix[x][y] <= matrix[i][j]: continue
                dp[i][j] = max(dp[i][j], backTrack(x, y))
            dp[i][j] = dp[i][j] + 1
            return dp[i][j]

        for i in range(M):
            for j in range(N):
                res = max(res, backTrack(i, j))
        return res