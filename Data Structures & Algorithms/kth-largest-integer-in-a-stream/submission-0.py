import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # min heap
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        #add the value
        heapq.heappush(self.nums, val) 

        #return the kth largest int => smallest from top k
        if len(self.nums) > self.k:
            heapq.heappop(self.nums) #make sure to only have k elements
        return self.nums[0] #return min element among the top k

        
