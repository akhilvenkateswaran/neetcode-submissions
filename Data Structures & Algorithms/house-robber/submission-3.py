class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if not nums:
            return 0

        if n == 1:
            return nums[0]
        maxAmount = [0] * (n)

        maxAmount[0] = nums[0]
        maxAmount[1] = max(nums[0],nums[1])

        for i in range(2,n):
            maxAmount[i] = max(maxAmount[i-1], nums[i]+maxAmount[i-2])
        
        print(maxAmount)
        return maxAmount[-1]