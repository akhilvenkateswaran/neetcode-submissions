class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [0] * (n+1)

        for i in range(2,len(cost)+1):
            res[i] = min((cost[i-1] + res[i-1]), (cost[i-2] + res[i-2]))

        return res[n]