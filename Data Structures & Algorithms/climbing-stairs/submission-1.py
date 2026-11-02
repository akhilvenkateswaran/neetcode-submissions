class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n+1)

        res[0] = 1
        res[1] = 1

        if n == 1 or n==2:
            return n

        for i in range(2,n+1):
            res[i] = res[i-1] + res[i-2]
        return res[-1]