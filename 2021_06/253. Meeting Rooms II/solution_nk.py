from collections import deque

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        q = deque()
        result = 0
        for i in intervals:
            n = len(q)
            count = 0
            while n != count:
                tmp = q.popleft()
                if tmp > i[0]:
                    q.append(tmp)
                count += 1
            q.append(i[1])
            result = max(result, len(q))
           
        return result
