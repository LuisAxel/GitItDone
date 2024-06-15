# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        ptr1 = dummy

        # Start point of reversed part
        for i in range(left - 1):
            ptr1 = ptr1.next

        cur = ptr1.next
        aux = cur

        # Reverse node by node
        for i in range(right - left):
            aux = cur.next
            cur.next = aux.next
            aux.next = ptr1.next
            ptr1.next = aux

        return dummy.next
