class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)

        n1, n2 = len(str1), len(str2)

        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(n1,n2)]
