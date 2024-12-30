class Solution:
    def decodeString(self, s: str) -> str:

        ans = []
        for char in s:

            if char == ']':
                decoding = ""
                while ans and ans[-1] != "[":
                    decoding = ans.pop() + decoding
                ans.pop()

                times = ""
                while ans and ans[-1].isdigit():
                    times = ans.pop() + times

                ans.append(decoding * int(times))
            else:
                ans.append(char)

       return "".join(ans)
