class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()
        for i in nums:
            duplicateSet.add(i)
        
        return len(nums) != len(duplicateSet)