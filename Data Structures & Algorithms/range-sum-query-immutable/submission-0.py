class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        prefixValue = 0
        for i in range(len(nums)):
            prefixValue = prefixValue + nums[i]
            self.prefix[i] = prefixValue
        print(self.prefix)
        

    def sumRange(self, left: int, right: int) -> int:

        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left -1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)