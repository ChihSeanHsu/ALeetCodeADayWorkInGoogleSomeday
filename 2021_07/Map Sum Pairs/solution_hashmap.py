from collections import defaultdict

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.score = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        ori_val = self.dict.get(key, 0)
        for idx in range(1, len(key) + 1):
            self.score[key[:idx]] += val - ori_val
        self.dict[key] = val

    def sum(self, prefix: str) -> int:
        return self.score.get(prefix, 0)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
