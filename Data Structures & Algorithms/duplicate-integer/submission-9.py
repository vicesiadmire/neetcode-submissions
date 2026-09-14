class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     nums_test = set(nums)
    #     if len(nums_test) < len(nums):
    #         return True
    #     else:
    #         return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        """this function will return whether there are duplicate values with 
        the number list. the set() data type ensures that the returned group
        of numbers only containes unique values. Comparing the set-ified list length
        vs the original list length will show quickly whether there are duplicates
        because the length would have changed between the two if duplicate
        values were in the original list
        """

        # changed from return True if len(nums) > len(set(nums)) else False
        # because why bother writing an if else? the logic will return
        # True or False just by doing the comparison
        return len(nums) > len(set(nums)) 