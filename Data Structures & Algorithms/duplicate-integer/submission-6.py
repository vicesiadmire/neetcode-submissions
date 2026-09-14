class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_test = set(nums)
        if len(nums_test) < len(nums):
            return True
        else:
            return False