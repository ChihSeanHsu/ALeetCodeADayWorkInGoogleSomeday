"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:    
        employee_mapping = {}
        stack = [id]
        result = 0
        
        for e in employees:
            employee_mapping[e.id] = e
        
        
        while stack:
            e_id = stack.pop()
            e_obj = employee_mapping[e_id]
            result += e_obj.importance
            if e_obj.subordinates:
                stack.extend(e_obj.subordinates)
        
        return result
        
    
        
