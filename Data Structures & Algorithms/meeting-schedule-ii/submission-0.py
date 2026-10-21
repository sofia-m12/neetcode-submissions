"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: #empty list case
            return 0
        intervals.sort(key=lambda x: x.start) #sort by start time
        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)

        for i in intervals[1:]:
            if min_heap[0] <= i.start: #dont need the room anymore/not occupied
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, i.end) #add current end time
            
        return len(min_heap) #heap has the min number of rooms occupied at last element
        