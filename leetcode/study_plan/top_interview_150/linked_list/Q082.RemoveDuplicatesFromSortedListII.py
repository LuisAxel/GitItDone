# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        p = dummy
        uk = dif = dummy.next

        while uk:
            while dif and uk.val == dif.val:
                dif = dif.next
            if uk.next != dif:
                p.next = dif
            else:
                p = uk
            uk = dif

        return dummy.next
