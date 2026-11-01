class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]

        curMax, curMin = 1,1

        for n in nums:
            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp, curMin * n, n)
            print(curMax,curMin)
            res = max(res,curMax)
        return res