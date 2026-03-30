class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            diff = target - nums[i] # 4
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i, j]

        