import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use a max heap, with length k
        #store elements in the heap along with their frequency
        #get (freq, elem) count first
        counts = Counter(nums)

        h = [] #empty heap
        #iterate thru array
        for n in counts.keys():
            # add n with count to heap
            heapq.heappush(h, (counts[n], n)) #this sorts by counts[n]
            if len(h) > k:
                heapq.heappop(h)
            #if heap has k elements, pop the smallest?
            #compare with current to see waht gets pushed
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1]) #[1] to reutrn n and NOT its count
        return res

        
        
        