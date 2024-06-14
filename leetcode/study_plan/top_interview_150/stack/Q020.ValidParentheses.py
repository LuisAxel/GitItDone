class Solution:
    def isValid(self, s: str) -> bool:

        seen = []
        pair = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in ['(', '[', '{']:
                seen.append(i)
            else:
                if not seen or pair[i] != seen.pop():
                    return False

        return True if not seen else False
