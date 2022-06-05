import bisect
import heapq

class MedianFinder:

    def __init__(self):
        self.stack = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.stack, num)

    def findMedian(self) -> float:
        n = len(self.stack)
        mid = n//2
        if n % 2:
            return self.stack[mid]
        else:
            return (self.stack[mid] + self.stack[mid - 1]) / 2
        
        
class MedianFinder:

    def __init__(self):
        # max heap
        self.left = []
        # min heap
        self.right = []
        
    def addNum(self, num: int) -> None:
        if len(self.right) == len(self.left):
            heapq.heappush(self.left, -heapq.heappushpop(self.right, num))
        else:
            heapq.heappush(self.right, -heapq.heappushpop(self.left, -num))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] + -self.left[0]) / 2
        else:
            return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
