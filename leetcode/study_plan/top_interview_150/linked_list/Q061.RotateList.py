# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        dummy.next = head

        n = 0
        cur = dummy
        while cur.next:
            cur = cur.next
            n += 1

        cur.next = dummy.next
        cur = dummy
        k = k % n

        for i in range(n - k):
            cur = cur.next

        dummy.next = cur.next
        cur.next = None

        return dummy.next
