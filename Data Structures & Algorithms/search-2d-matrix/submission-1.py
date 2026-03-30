class Solution:

    def binarySearch(self, left, matrix, target):
        i = 0
        r = len(matrix[0]) - 1
        while i <= r:
            mid = int((i + r)/2)
            
            if target == matrix[left][mid]:
                return True
            elif target > matrix[left][mid]:
                i = mid + 1
            else:
                r = mid - 1
            
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        colI = 0
        colJ = len(matrix) - 1

        while colI < colJ:
            mid = int((colI + colJ + 1)/2)

            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                colI = mid
            else:
                colJ = mid - 1
        
        return self.binarySearch(colI, matrix, target)
