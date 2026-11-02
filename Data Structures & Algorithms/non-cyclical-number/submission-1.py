class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while(n not in seen):
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, number: int) -> int: 
        temp = number
        sum = 0
        while temp > 0:
            rem = temp % 10
            sum += (rem*rem)
            temp = temp//10
        return sum