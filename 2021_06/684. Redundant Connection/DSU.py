from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num = len(edges)
        parents = list(range(num))
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            parents[x] = parents[y]
        
        for e in edges:
            x = find(e[0] - 1)
            y = find(e[1] - 1)
            
            if x == y:
                return e
            union(x, y)
            
