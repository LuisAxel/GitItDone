class Solution:
    def gcd(a: int, b: int) -> int:
        return a if b == 0 else gcd(b, a % b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return "" if str1 + str2 != str2 + str1 else str1[:gcd(len(str1), len(str2))]
