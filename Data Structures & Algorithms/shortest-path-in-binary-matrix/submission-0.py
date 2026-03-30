from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROW_LENGTH = len(grid)
        COL_LENGTH = len(grid[0])
        visited = set()
        queue = deque()

        # If top left or bottom right is 1 there wont be any path
        if grid[0][0] or grid[ROW_LENGTH - 1][COL_LENGTH - 1]:
            return -1

        queue.append((0,0))
        visited.add((0,0))

        shortest_length = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # If the poped element is bottom right element return the length
                if r == ROW_LENGTH - 1 and c == COL_LENGTH - 1:
                    return shortest_length

                # If not bottom right append all the elements to the queue
                directions = [[-1, 0],[1,0],[0,1],[1,0],[1,1],[-1,1],[1, -1], [-1, -1]]
                for dr, dc in directions:
                    row, column = r + dr, c + dc
                    
                    if row not in range(ROW_LENGTH) or column not in range(COL_LENGTH) or (row, column) in visited or grid[row][column] == 1:
                        continue

                    queue.append((row, column))
                    visited.add((row, column))
            shortest_length = shortest_length + 1
        return -1
        