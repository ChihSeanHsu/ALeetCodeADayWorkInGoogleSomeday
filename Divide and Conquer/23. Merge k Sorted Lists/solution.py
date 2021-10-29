import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0]
        
    def merge2Lists(self, list1, list2)-> Optional[ListNode]:
        head = curr = ListNode(0)
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
                
            curr = curr.next
            
        if list1:
            curr.next = list1
        
        if list2:
            curr.next = list2
                
        return head.next      
