# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1 = ListNode(0,None)
        d2 = ListNode(0,None)
        l1, l2 = d1, d2

        cur = head
        while cur:
            # Sublist for < val
            if cur.val < x:
                l1.next = cur
                l1 = l1.next
            # Sublist for >= val
            else:
                l2.next = cur
                l2 = l2.next
            cur = cur.next

        # Combine lists and end possible cycle
        l1.next = d2.next
        l2.next = None

        return d1.next
