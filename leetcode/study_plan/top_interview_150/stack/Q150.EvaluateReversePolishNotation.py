class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def pop(s):
            return int(s.pop())
        s = []
        op1 = 0

        for i in tokens:
            if i == '+':
                s.append(pop(s) + pop(s))
            elif i == '-':
                op1 = pop(s)
                s.append(pop(s) - op1)
            elif i == '*':
                s.append(pop(s) * pop(s))
            elif i == '/':
                op1 = pop(s)
                s.append(int(pop(s) / op1))
            else:
                s.append(i)
        return int(s[0])
