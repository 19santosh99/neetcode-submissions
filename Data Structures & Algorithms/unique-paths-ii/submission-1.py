class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])

        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[ROW - 1][COL - 1] == 1:
                return 0

        def dfs(r, c, grid):
            if r >= ROW or c >= COL or obstacleGrid[r][c] == 1:
                return 0
            
            if grid[r][c] != -1:
                return grid[r][c]

            if r == ROW - 1 and c == COL - 1:
                return 1

            grid[r][c] = dfs(r + 1,c, grid) + dfs(r,c + 1,grid)
            return grid[r][c]

        return dfs(0,0,[[-1]* COL for _ in range(ROW)])
        