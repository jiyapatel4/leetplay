class Solution():
    def canCompleteCicuit(self, gas, cost):
        if len(gas) == 1:
            if (gas[0] >= cost[0]):
                return 0
            else:
                return -1
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start
