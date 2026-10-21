import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #need to order stones to determine the heviest -> max heap
        stones_heap = [-w for w in stones]# negatives for max heap
        heapq.heapify(stones_heap) #convert to heap

        #loop until no more stones in the heap
        while len(stones_heap) > 1:
            #get the 2 heaviest
            first = -heapq.heappop(stones_heap)
            second = -heapq.heappop(stones_heap)

            #compare, update the heap if needed
            if first > second:
                #add new wight back to the heap
                heapq.heappush(stones_heap, -(first - second))

        return -stones_heap[0] if len(stones_heap) else 0