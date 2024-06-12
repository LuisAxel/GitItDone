class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        canDo = 0
        fuel = 0
        station = 0
        n = len(gas)

        for i in range(0, n):
            canDo += gas[i] - cost[i]
            fuel += gas[i] - cost[i]
            # Cannot start from [initial_station:this_station], try next one
            if fuel < 0:
                fuel = 0
                station = i + 1

        if canDo < 0:
            return -1
