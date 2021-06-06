from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node_to_node = defaultdict(set)

        def dfs(x, y):
            if x not in visited:
                
                if x == y:
                    return True
                visited.add(x)
                return any(dfs(nei, y) for nei in node_to_node[x])
                
        
        for x, y in edges:
            visited = set()
            if x in node_to_node and y in node_to_node and dfs(x, y):
                return [x, y]

            node_to_node[x].add(y)
            node_to_node[y].add(x)
                    
        
            
