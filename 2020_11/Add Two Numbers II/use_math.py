# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = l1
        second = l2
        f = int()
        s = int()
        while first or second:
            if first:
                f = f * 10 + first.val
                first = first.next
            if second:
                s = s * 10 + second.val
                second = second.next

        value = f + s
        ans = None
        while value:
            tmp = ListNode(value % 10)
            value //= 10
            tmp.next= ans
            ans = tmp
        if ans is None:
            ans = ListNode()
        return ans
