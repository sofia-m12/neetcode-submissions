import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # kth largest = smallest of the top k
        # create a min heap with the top k
        heapq.heapify(self.nums)
        while len(self.nums) > k: #only keep k elements in the heap
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # add to the stream
        heapq.heappush(self.nums, val)
        # correct (k elements in the heap)
        while len(self.nums) > self.k: #only keep k elements in the heap
            heapq.heappop(self.nums)
        #return the top/first of the heap(kth largest element)
        return self.nums[0]
        
