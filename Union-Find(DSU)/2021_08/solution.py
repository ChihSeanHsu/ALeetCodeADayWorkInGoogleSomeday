from collections import defaultdict

class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def add(self, x):
        self.parent[x] = x
        self.size[x] = 1
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.size[y] += self.size[x]
        self.parent[x] = y
        
    def groups(self):
        group = defaultdict(list)
        for x in self.parent.keys():
            group[self.find(x)].append(x)
        return group
        

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        mapping = defaultdict(list)
        
        for row in range(n):
            for col in range(m):
                mapping[matrix[row][col]].append((row, col))
        
        for d in sorted(mapping.keys()):
            dsu = DSU()
            
            for i, j in mapping[d]:
                j += n
                dsu.add(i)
                dsu.add(j)
            
            for i,j in mapping[d]:
                j += n
                dsu.union(i, j)
            
            for values in dsu.groups().values():
                max_rank = 0
                for i in values:
                    max_rank = max(max_rank, rank[i])
                for i in values:
                    rank[i] = max_rank + 1
                    
                for i, j in mapping[d]:
                    matrix[i][j] = rank[i]
            
        return matrix
            
            
        
        
        
                
