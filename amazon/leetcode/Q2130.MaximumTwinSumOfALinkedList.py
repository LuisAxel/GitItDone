# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = prev = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        half = None
        while slow:
            tmp = slow.next
            slow.next = half
            half = slow
            slow = tmp

        prev.next = half

        ans = 0
        while half:
            ans = max(ans, half.val + head.val)
            half = half.next
            head = head.next
        return ans
