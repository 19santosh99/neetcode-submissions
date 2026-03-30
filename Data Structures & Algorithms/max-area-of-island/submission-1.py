class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROW_SIZE = len(grid)
        COL_SIZE = len(grid[0])
        visited = set()
        island_max_size = 0

        def dfs(r,c):
            if r not in range(ROW_SIZE) or c not in range(COL_SIZE) or (r,c) in visited or grid[r][c] == 0:
                return 0
            count = 0
            visited.add((r,c))
            
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            return 1 + count




        for i in range(ROW_SIZE):
            for j in range(COL_SIZE):
                if grid[i][j] == 1 and (i,j) not in visited:
                    island_size = dfs(i,j)
                    island_max_size = max(island_max_size, island_size)
        return island_max_size
        