class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i,n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                stackVal, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            else:
                stack.append((n,i))
        return result
    
        