class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        stones = [ num * -1 for num in stones ] # [-1, -3]
        heapq.heapify(stones)
        
        while len(stones) >= 2: #5 > 2
            largest = heapq.heappop(stones) # -6 
            s_largest = heapq.heappop(stones) # -4

            if largest != s_largest: 
                heapq.heappush(stones, largest - s_largest) # [-2, -2, -2, -3]

        return 0 if len(stones) == 0 else stones[0]* -1
        