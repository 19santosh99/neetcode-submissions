class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data_set = {}
        for num in nums:
            if num in data_set:
                return True
            
            data_set[num] = 1
        return False
         