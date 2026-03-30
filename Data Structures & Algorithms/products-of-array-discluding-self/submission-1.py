class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        #prefix sums
        for i in range(1, len(nums)):
            prev_product = prefix[i-1] * nums[i-1]
            prefix[i] = prev_product

        # suffix sum [1,2,3,4] [0,1,2,3]
        for i in range(len(nums) - 2, -1, -1):
            prev_product = suffix[i+1] * nums[i+1]
            suffix[i] = prev_product

        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])
        return ans

            