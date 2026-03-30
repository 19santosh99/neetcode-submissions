from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicto = defaultdict(int)

        for num in nums:
            if num in dicto:
                dicto[num] += 1
            else:
                dicto[num] = 1

        ans = []

        for key, value in dicto.items():
            heapq.heappush(ans, (value, key))

        result = heapq.nlargest(k, ans)
        final = []
        for tup in result:
            final.append(tup[1])
        return final


        