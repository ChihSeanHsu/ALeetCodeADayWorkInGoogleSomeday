# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        sequence = [head]
        cursor = head.next
        while cursor:
            found = False
            stack = []
            while not found and sequence:
                t = sequence.pop()
                if t.val < cursor.val:
                    found = True
                else:
                    stack.append(t)
            else:

                stack.append(cursor)
                if found:
                    stack.append(t)
                

            s= list(reversed(stack))
            sequence.extend(s)
            cursor = cursor.next

        new_head = sequence[0]
        tmp = new_head
        for i in sequence[1:]:
            tmp.next = i
            tmp = i
        tmp.next = None
        
            
        
        return new_head
