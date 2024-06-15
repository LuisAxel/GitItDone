# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        ptr1 = dummy

        cur = ptr1.next
        aux = cur
        valid = True

        while valid:
            cur = ptr1.next
            # Reverse node by node
            for i in range(k - 1):
                aux = cur.next
                cur.next = aux.next
                aux.next = ptr1.next
                ptr1.next = aux
            ptr1 = cur
            # do we have k more pairs?
            for i in range(k):
                ptr1 = ptr1.next
                if not ptr1:
                    valid = False
                    break
            ptr1 = cur

        return dummy.next
