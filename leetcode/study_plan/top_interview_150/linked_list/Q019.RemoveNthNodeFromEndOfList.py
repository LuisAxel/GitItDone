# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        delete = end = dummy

        for i in range(n):
            end = end.next

        while end.next:
            end = end.next
            delete = delete.next

        delete.next = delete.next.next

        return dummy.next
