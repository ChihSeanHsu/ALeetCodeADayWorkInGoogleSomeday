# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # time: O(max(m, n)) space: O(m+n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        ptr1 = headA
        ptr2 = headB
        while headA or headB:
            if headA:
                if headA in seen:
                    return headA
                seen.add(headA)
                headA = headA.next
                
            if headB:
                if headB in seen:
                    return headB
                seen.add(headB)
                headB = headB.next
            
        return None
      
    # time: O(m+n) space: O(1)
    # They will finally meet because nodeA and nodeB will run len(headA) + len(headB) and if they don't meet, it mean they don't intersect
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        
        return nodeA
        
