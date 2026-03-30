class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_ans = {}
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in set_ans:
                return [set_ans.get(diff), i]
            else:
                set_ans[num] = i


        