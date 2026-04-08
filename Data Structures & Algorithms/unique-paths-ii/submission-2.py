class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])
        
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[ROW - 1][COL - 1] == 1:
            return 0

        prevRow = [0] * COL

        for i in range(ROW - 1, -1, -1):
            currRow = [0] * COL

            if obstacleGrid[i][COL - 1] != 1:
                if i == ROW - 1:
                    currRow[COL - 1] = 1
                else:
                    currRow[COL - 1] = prevRow[COL - 1]

            for j in range(COL - 2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    currRow[j] = prevRow[j] + currRow[j + 1]
                
            prevRow = currRow
        return prevRow[0]

            

        