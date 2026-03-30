class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        count = [0] * 3
        for i in nums:
            count[i] = count[i] + 1
        
        i = 0
        for j, n in enumerate(count):
            for _ in range(0, n):
                nums[i] = j
                i = i + 1