'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0), ]
        landIdArea, ROWS, COLS = defaultdict(int), len(grid), len(grid[0])

        def colorLand(r, c, seen, landId=2):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1 and (r, c) not in seen:
                grid[r][c] = landId
                landIdArea[landId] += 1
                seen.add((r, c))
                for x, y in MOVES:
                    rn = r + x
                    cn = c + y
                    colorLand(rn, cn, seen, landId)

        def trySwapAndCalculateArea(r, c):
            landIdSeen = set()
            formedArea = 0
            for x, y in MOVES:
                rn = r + x
                cn = c + y
                if 0 <= rn < ROWS and 0 <= cn < COLS and grid[rn][cn] != 0:
                    landId = grid[rn][cn]
                    if landId not in landIdSeen:
                        landIdSeen.add(landId)
                        formedArea += landIdArea[landId]
            return formedArea

        landId = 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    landId += 1
                    colorLand(r, c, set(), landId)

        totalArea, zeroFound = 0, False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    zeroFound = True
                    formedArea = trySwapAndCalculateArea(r, c)
                    totalArea = max(totalArea, formedArea)
        return totalArea + 1 if zeroFound else ROWS * COLS