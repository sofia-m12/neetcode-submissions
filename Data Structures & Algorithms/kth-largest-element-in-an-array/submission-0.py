import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [] #push the negatives
        for n in nums:
            heapq.heappush(max_heap, -n) #add to heap
        
        for _ in range(k-1):
            heapq.heappop(max_heap)

        return  -1 * heapq.heappop(max_heap) #return kth largest


