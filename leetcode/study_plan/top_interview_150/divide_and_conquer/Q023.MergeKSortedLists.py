# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            dummy = cur = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next

            # One list could be larger
            cur.next = list1 or list2
            return dummy.next

        def mergeSort(lists, start, end):
            if start == end:
                return lists[start]

            mid = (start + end) // 2

            left = mergeSort(lists, start, mid)
            right = mergeSort(lists, mid + 1, end)

            return merge(left, right)

        if not lists:
            return None
        return mergeSort(lists, 0, len(lists) - 1)

