class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # we need to have global max and current count
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):

            # Kadens algo says, for each num either we start from there or add to the current sum
            currSum = max(nums[i], currSum + nums[i])

            #calculate max of current sum and max sum for every stage
            maxSum = max(currSum, maxSum)

        return maxSum
            
        