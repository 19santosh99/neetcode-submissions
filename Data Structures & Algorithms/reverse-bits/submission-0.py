class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        new_num = 0
        for i in range(32):
            if n & 1:
                shift_by = 32 - i - 1
                result |= 1 << shift_by
            n = n >> 1
        return result
