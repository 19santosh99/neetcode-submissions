class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(r,c, visited):
            ROW_SIZE = len(grid)
            COL_SIZE = len(grid[0])
            # Base Case
            # return cound 0 for not valid cases
            if (r < 0 or c < 0) or (r >= ROW_SIZE or c >= COL_SIZE) or grid[r][c] == 1 or (r,c) in visited:
                return 0

            # if we reach end of the matrix that means
            # we reached from the top left to bottom right so return 1
            if r == ROW_SIZE - 1 and c == COL_SIZE - 1:
                return 1

            visited.add((r,c))
            count = 0
            #Traversing
            count += dfs(r + 1, c, visited)
            count += dfs(r - 1, c, visited)
            count += dfs(r, c + 1, visited)
            count += dfs(r, c - 1, visited)

            #backtrack
            visited.remove((r,c))
            return count

        
        
        return dfs(0,0,set())
        