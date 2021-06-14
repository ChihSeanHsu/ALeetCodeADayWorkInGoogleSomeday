import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        q = []
        for start, end in intervals:
            if q and q[0] <= start:
                heapq.heappop(q)
            heapq.heappush(q, end)
        return len(q)
