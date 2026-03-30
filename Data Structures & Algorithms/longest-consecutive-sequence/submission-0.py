class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length = length + 1
                max_len = max(max_len , length)
        return max_len