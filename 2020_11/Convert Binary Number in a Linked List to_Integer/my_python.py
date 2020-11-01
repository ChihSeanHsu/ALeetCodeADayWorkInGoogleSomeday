# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        tmp = head
        value_list = []
        while tmp:
            value_list.append(tmp.val)
            tmp = tmp.next

        result = 0
        for idx, i in enumerate(value_list[::-1]):
            result += i * (2 ** idx)
        return result
