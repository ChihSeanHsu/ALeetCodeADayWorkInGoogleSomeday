# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # two time pass
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idx = 1
        critical = []
        prev = head
        curr = head.next
        while curr.next:
            if prev.val > curr.val and curr.next.val > curr.val:
                critical.append(idx)
            if prev.val < curr.val and curr.next.val < curr.val:
                critical.append(idx)
            
            idx += 1
            prev = curr
            curr = curr.next
        
        if len(critical) < 2:
            return [-1, -1]
        
        maxima = critical[-1] - critical[0]
        minima = float("inf")
        for i in range(len(critical) - 1):
            minima = min(minima, critical[i + 1] - critical[i])
        
        return [minima, maxima]
    
    
    
    # one-time pass
    def is_critical(self, prev, curr) -> bool:
        return (prev.val > curr.val and curr.next.val > curr.val) or (prev.val < curr.val and curr.next.val < curr.val)
    
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idx = 1
        prev = head
        curr = head.next
        prev_cri = 0
        maxima = 0
        minima = float("inf")
        while curr.next:
            if self.is_critical(prev, curr):
                if prev_cri:
                    dist = idx - prev_cri
                    minima = min(minima, dist)
                    maxima += dist
                prev_cri = idx
                
            idx += 1
            prev = curr
            curr = curr.next
        
        return [minima, maxima] if maxima != 0 else [-1, -1]
            
            
