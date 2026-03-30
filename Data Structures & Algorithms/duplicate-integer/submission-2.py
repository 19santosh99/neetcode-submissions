class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_arr = set()
        for num in nums:
            if num not in set_arr:
                set_arr.add(num)
            else:
                return True
        return False
        