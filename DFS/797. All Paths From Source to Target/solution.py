from collecions import deque

class Solution:
    # bfs
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque()
        q.append([0])
        
        output = []
        while q:
            path = q.popleft()
            last_node = path[-1]
            if last_node == len(graph) - 1:
                output.append(path)
                continue
                
            for node in graph[last_node]:
                q.append(path.copy() + [node])
            
        return output
    
    # dfs
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        def dfs(node: int, path: List[List[int]]):
            if node == len(graph) - 1:
                output.append(path + [node])
                return
            
            path.append(node)
            for n in graph[node]:
                dfs(n, path)
            path.pop()
        
        dfs(0, [])
        return output
