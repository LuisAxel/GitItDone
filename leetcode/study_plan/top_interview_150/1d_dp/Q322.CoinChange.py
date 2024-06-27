class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initially cant give change
        can_do = [float('inf')] * (amount + 1)
        # Base case, change of 0 is 0 coins
        can_do[0] = 0

        # Bottom up, build changes
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    can_do[i] = min(can_do[i], can_do[i - coin] + 1)

        return -1 if can_do[-1] == float('inf') else can_do[-1]
