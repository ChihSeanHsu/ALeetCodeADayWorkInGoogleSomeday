class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = list()
        stack.append(intervals[0])
        for i in intervals[1:]:
            last = stack[-1]
            if i[0] <= last[1]:
                last[1] = max(last[1], i[1])
            else:
                stack.append(i)
        return stack
