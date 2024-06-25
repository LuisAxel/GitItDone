class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1, n2 = len(a) - 1, len(b) - 1
        # Let a be smallest
        if n1 > n2:
            n1, n2 = n2, n1
            a, b = b, a

        i = 0
        carry = 0
        ans = deque()
        while i <= n1:
            carry += int(a[n1 - i])
            carry += int(b[n2 - i])
            ans.appendleft(str(carry % 2))
            carry //= 2
            i += 1

        while i <= n2:
            carry += int(b[n2 - i])
            ans.appendleft(str(carry % 2))
            carry //= 2
            i += 1

        if carry != 0:
            ans.appendleft(str(carry % 2))

        return ''.join(ans)


