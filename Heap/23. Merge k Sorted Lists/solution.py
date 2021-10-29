import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for h in lists:
            tmp = h
            while tmp:
                heapq.heappush(heap, tmp.val)
                tmp = tmp.next
                
        if not heap:
            return 
        
        num = heapq.heappop(heap)
        head = ListNode(num)
        curr = head
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
            
        return head
