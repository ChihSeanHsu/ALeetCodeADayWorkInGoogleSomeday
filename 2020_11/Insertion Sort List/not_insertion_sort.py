# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        tmp = head
        store = []
        while tmp:
            store.append(tmp)
            tmp = tmp.next
        order = sorted(store, key=lambda x: x.val)
        tmp = new_head = order[0]
        new_head.next = None
        for i in order[1:]:
            tmp.next = i
            tmp = i
        tmp.next = None
        return new_head
