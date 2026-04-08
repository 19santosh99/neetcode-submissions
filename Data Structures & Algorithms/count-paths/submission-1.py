class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prevRow = [0] * n

        for i in range(m-1,-1,-1):
            currRow = [0] * n

            # from final destination to final destination no of ways is 1
            currRow[n - 1] = 1

            for j in range(n - 2, -1, -1):
                currRow[j] = currRow[j + 1] + prevRow[j]

            prevRow = currRow
        return prevRow[0]
        