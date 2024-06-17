"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
             return None

        original = head
        copy = None
        # Embedding copy in original
        # OG(1)->CP(1)->OG(2)->CP(2)....
        while original:
            copy = Node(original.val)
            copy.next = original.next
            original.next = copy
            original = copy.next

        original = head
        # Assigning Randoms
        # OG(R+1)=CP(R)
        while original:
            if original.random:
                original.next.random = original.random.next
            original = original.next.next

        original = head
        ans = head.next
        # Separating Lists
        while original:
            copy = original.next
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next

        return ans
