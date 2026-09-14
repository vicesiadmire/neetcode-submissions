class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > 0:
            for num in nums:
                if (nums.count(num) > 1):
                    val = True
                    break
                else:
                    val = False
        else:
            val = False

        return val
            
            

            
         