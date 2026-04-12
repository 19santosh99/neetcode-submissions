class Solution:
    def hammingWeight(self, n: int) -> int:
        count_of_ones = 0
        while n > 0:
            if n & 1 == 1:
                count_of_ones = count_of_ones + 1
            n = n >> 1
        return count_of_ones

        