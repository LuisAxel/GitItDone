class Solution:
    def intToRoman(self, num: int) -> str:
        values = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, 
                  "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

        ans = ""
        for key, value in values.items():
            ans += key * (num // value)
            if num // value > 0:
                num -= (value * (num // value))
        return ans
