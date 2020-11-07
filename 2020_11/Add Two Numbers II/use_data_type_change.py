# not a good solution, waste lot of time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = l1
        second = l2
        first_str = ''
        second_str = ''
        while first or second:
            if first:
                first_str += str(first.val)
                first = first.next
            if second:
                second_str += str(second.val)
                second = second.next
                
        answer = str(int(first_str) + int(second_str))
        head = ListNode(int(answer[0]))
        tmp = head
        for i in answer[1:]:
            t = ListNode(int(i))
            tmp.next = t
            tmp = t
        return head
