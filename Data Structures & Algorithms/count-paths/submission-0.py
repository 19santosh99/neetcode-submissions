class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]

        def dfs(r,c, grid):
            # Base Case
            # if the co-ords go out of bounds return 0
            if r >= m or c >=n:
                return 0

            if grid[r][c] != 0:
                return grid[r][c]

            if r == m-1 and c == n-1:
                return 1


            grid[r][c] = dfs(r + 1, c, grid) + dfs(r, c + 1, grid)
            return grid[r][c]


        return dfs(0,0, grid)
        