class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        maxSum, minSum = nums[0], nums[0]
        currMax, currMin = nums[0], nums[0]
        total = nums[0]

        for num in nums[1:]:
            currMax = max(num, num + currMax)
            currMin = min(num, num + currMin)
            total += num

            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)

        return max(total - minSum, maxSum) if maxSum > 0 else maxSum