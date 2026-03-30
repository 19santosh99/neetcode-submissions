import math
class Solution:
    def tempFunc(self, k, h, piles):
        totalHrs = 0
        for num in piles:
            totalHrs = totalHrs + math.ceil(num/k)

        if totalHrs > h:
            return False
        elif totalHrs <= h:
            return True
            



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        lastMid = math.inf

        while left <= right:

            mid = left + ((right - left)// 2)

            if self.tempFunc(mid, h, piles):
                lastMid = min(mid, lastMid)
                right = mid - 1
            else:
                left = mid + 1
                

        return lastMid


            
        