'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, seen):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1' and (r, c) not in seen:
                seen.add((r, c))
                for move in MOVES:
                    rn = r + move[0]
                    cn = c + move[1]
                    dfs(rn, cn, seen)

        count, seen = 0, set()
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == '1':
                    dfs(r, c, seen)
                    count += 1
        return count
