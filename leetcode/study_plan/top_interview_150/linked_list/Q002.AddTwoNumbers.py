# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, n, m = 0, 0, 1
        p1 = l1
        while p1 != None:
            n += p1.val * m
            m *= 10
            p1 = p1.next
        ans += n

        n, m = 0, 1
        p1 = l2
        while p1 != None:
            n += p1.val * m
            m *= 10
            p1 = p1.next
        ans += n

        head = res = ListNode(0)
        while res != None:
            res.val = ans % 10
            ans = ans // 10
            if ans > 0:
                res.next = ListNode()
            res = res.next
        return head
