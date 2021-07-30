from collections import defaultdict

class Trie:
    def __init__(self):
        self.score = 0
        self.children = defaultdict(Trie)

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        ori_val = self.dict.get(key, 0)
        curr = self.trie
        curr.score += val - ori_val
        for c in key:
            curr = curr.children[c]
            curr.score += val - ori_val
        self.dict[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.trie
        for c in prefix:
            curr = curr.children[c]
        return curr.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
