# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return 
        new_head, cursor = head, head.next
        new_head.next = None
        while cursor:
            new_head, cursor = self.compare(new_head, cursor)
            
        return new_head
    
    def compare(self, head: ListNode, cursor: ListNode) -> (ListNode, ListNode):
        if head is None:
            head, cursor = cursor, cursor.next
            head.next = None
        elif head.val > cursor.val:
            tmp = cursor.next
            cursor.next = head
            head, cursor = cursor, tmp
        else:
            head.next, cursor = self.compare(head.next, cursor)

        return head, cursor
