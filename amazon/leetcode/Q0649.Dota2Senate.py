class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)

        for idx, c in enumerate(senate):
            if c == 'R':
                radiant.append([idx, c])
            else:
                dire.append([idx, c])

        while radiant and dire:
            if radiant[0][0] < dire[0][0]:
                dire.popleft()
                next_turn = radiant.popleft()
                next_turn[0] += n
                radiant.append(next_turn)
            else:
                radiant.popleft()
                next_turn = dire.popleft()
                next_turn[0] += n
                dire.append(next_turn)

        return "Radiant" if radiant else "Dire"
