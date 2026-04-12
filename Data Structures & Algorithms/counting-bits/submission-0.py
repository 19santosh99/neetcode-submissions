class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(0,n+1):
            count = 0
            while num > 0:
                count += num & 1
                num = num >> 1
            output.append(count)
        return output

