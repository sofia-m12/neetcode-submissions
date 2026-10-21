import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #max heap
        stones = [-w for w in stones]
        heapq.heapify(stones) #O(N)

        #loop until len(stones) 1
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x < y:
                heapq.heappush(stones, x - y) # add back to the heap
        stones.append(0)
        return abs(stones[0])
        