# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            if l1:
                return l1
            elif l2:
                return l2
            else:
                return 
                     
        curr = ListNode()
        if l1.val <= l2.val:
            curr.val = l1.val
            l1 = l1.next
        else:
            curr.val = l2.val
            l2 = l2.next

        curr.next = self.mergeTwoLists(l1, l2)
        return curr
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = curr = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
                
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return result.next
        
