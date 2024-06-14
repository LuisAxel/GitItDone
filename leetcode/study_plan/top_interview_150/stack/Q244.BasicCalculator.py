class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        op = 1
        st = []

        s = s.replace(" ",'')
        for i in s:
            # Form digit
            if i.isdigit():
                num *= 10
                num += int(i)
            # Add sign to number formed and save sign for next number
            elif i in '+-':
                ans += num * op
                op = 1 if i == '+' else -1
                num = 0
            # Save answer so far and sign of ()
            elif i == '(':
                st.append(ans)
                st.append(op)
                ans = 0
                op = 1
            # get value of (), assign sign and add to answer
            else:
                ans += num * op
                ans *= st.pop()
                ans += st.pop()
                num = 0
        # Add last number to answer
        return ans + num * op
