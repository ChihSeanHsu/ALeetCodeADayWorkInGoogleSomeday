from collections import deque


class RecentCounter:

    def __init__(self):
        """
            I use list at first time I solve this question, but it need to l.pop(0) 
            and it need to move whole elements in list to their left side, it will casue some wasting.
            using deque make left pop more efficiently
        """
        self.ping_store = deque()

    def ping(self, t: int) -> int:
        lower = t - 3000
        self.ping_store.append(t)
        while lower > self.ping_store[0]:
            self.ping_store.popleft()
        return len(self.ping_store)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
