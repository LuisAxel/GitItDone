# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(head):
            # sort of x= 1 or 0 is x
            if not head or not head.next:
                return head

            mid, end = head, head.next
            while end and end.next:
                mid = mid.next
                end = end.next.next
            # Separate lists
            mid_r = mid.next
            mid.next = None

            left = mergeSort(head)
            right = mergeSort(mid_r)

            dummy = ListNode(0)
            cur = dummy

            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next

            # In case one half was bigger
            cur.next = left or right
            return dummy.next

        return mergeSort(head)
