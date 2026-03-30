from collections import deque
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROW_LENGTH = len(grid)
        COL_LENGTH = len(grid[0])
        queue = deque()
        fresh = 0
        time = 0

        for i in range(ROW_LENGTH):
            for j in range(COL_LENGTH):
                if grid[i][j] == 1:
                    fresh = fresh + 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    row, column = dr + r, dc + c
                    if row not in range(ROW_LENGTH) or column not in range(COL_LENGTH) or grid[row][column] == 0 or grid[row][column] == 2:
                        continue
                    grid[row][column] = 2
                    queue.append((row, column))
                    fresh = fresh - 1
            time = time + 1

        return time if fresh == 0 else -1
