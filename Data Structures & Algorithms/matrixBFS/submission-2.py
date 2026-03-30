from collections import deque

# [0, 0, 1]
# [0, 1, 0]
# [1, 0, 0]

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        ROW_LENGTH = len(grid)
        COL_LENGTH = len(grid[0])
        queue = deque()
        visited = set()

        if grid[0][0] == 1 or grid[ROW_LENGTH - 1][COL_LENGTH - 1] == 1:
            return -1

        #initially add the first point(top left index) to the queue
        queue.append((0,0))
        visited.add((0,0))

        shortest_length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # if the r,c is the bottom right return the length
                if r == ROW_LENGTH - 1 and c == COL_LENGTH - 1:
                    return shortest_length
                # else we need to check the neighbours
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    # see if the point is in the matrix if not just skip that point
                    # or if the grid value is 1 that means its blocked
                    # so do not add to the queue

                    if (r + dr not in  range(ROW_LENGTH)) or (c + dc not in range(COL_LENGTH)) or ((r + dr, c + dc) in visited) or (grid[r + dr][c + dc] == 1):
                        continue

                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            shortest_length = shortest_length + 1
        return -1