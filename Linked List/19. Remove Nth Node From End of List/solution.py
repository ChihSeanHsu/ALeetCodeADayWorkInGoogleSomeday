# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  
    # O(2n) O(n)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
            
        idx = 1
        next_node = None
        while idx != n:
            next_node = stack.pop()
            idx += 1
            
        stack.pop()
        
        if stack:
            stack[-1].next = next_node
            return head
            
        return next_node
    
    # O(n) O(n)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        ptr1 = head
        ptr2 = head
        count = 1
        
        while ptr1:
            if count >= n:
                stack.append(ptr2)
                ptr2 = ptr2.next
            ptr1 = ptr1.next
            count += 1
        
        stack.pop()
        if stack:
            stack[-1].next = ptr2
            return head
        return ptr2
    
     # O(n) O(1)
     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        end = head
        count = 1
        
        while n > count:
            end = end.next
            count += 1
        
        prev = None
        while end and end.next:
            end = end.next
            prev = front
            front = front.next
        
        if prev:
            prev.next = front.next
            return head
        
        return head.next
        
            
        
        
            
