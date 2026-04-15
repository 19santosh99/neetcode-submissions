
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i, num in enumerate(nums):
            # before Filling the window if we see the number again return
            if num in seen:
                return True

            # Fill in the window
            seen.add(num)

            # if the window is full pop leftmost element
            if len(seen) > k:
                seen.remove(nums[i-k])

        return False

        