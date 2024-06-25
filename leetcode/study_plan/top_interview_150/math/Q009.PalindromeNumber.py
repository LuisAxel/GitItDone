class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev *= 10
            rev += x % 10
            x //= 10
        # digits % 2 == 1, ignore middle number
        if rev > x:
            rev //= 10

        return x == rev
