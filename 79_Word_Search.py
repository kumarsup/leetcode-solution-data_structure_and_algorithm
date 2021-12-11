'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N, res = len(board), len(board[0]), False

        def isValidMove(i, j):
            return (i >= 0 and i < M and j >= 0 and j < N)

        def backtrack(row, col, suffix):
            nonlocal res, moves

            if len(suffix) == 0:
                return True

            if isValidMove(row, col) is False or board[row][col] != suffix[0]:
                return False

            ret = False
            board[row][col] = '#'

            for x, y in moves:
                ret = backtrack(row + x, col + y, suffix[1:])
                if ret: break
            board[row][col] = suffix[0]
            return ret

        for row in range(M):
            for col in range(N):
                if backtrack(row, col, word):
                    return True
        return False