class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW_SIZE = len(grid)
        COL_SIZE = len(grid[0])

        count = 0
        visited = set()

        def dfs(r, c, visited):
            if not (0 <= r < ROW_SIZE) or not (0 <= c < COL_SIZE) or (r,c) in visited or grid[r][c] == "0":
                return


            visited.add((r,c))
            

            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

        
        for i in range(ROW_SIZE):
            for j in range(COL_SIZE):
                if not grid[i][j] == "0" and (i,j) not in visited:
                    dfs(i,j, visited)
                    count = count + 1
        
        return count
        