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