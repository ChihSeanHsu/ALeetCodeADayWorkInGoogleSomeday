class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = []
        stack.extend(rooms[0])
        while stack:
            key = stack.pop()
            visited.add(key)
            for k in rooms[key]:
                if not k in visited:
                    stack.append(k)
                    
        return len(visited) == len(rooms)
            
            
