class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        conclusion = []
        nums_diff = []

        i = 0
        while i < len(nums):
            
            #find the difference between target num and list num
            difference = target - nums[i]

            #build a hash_map(dict) out of the nums list to access
            ##data there later
            if nums[i] in hash_map:
                hash_map['same'] = i
            else: 
                hash_map[nums[i]] = i

            #add a list of the found differences to be accessed later
            if difference in nums:
                nums_diff.append(difference)

            i = i + 1
        
        if len(nums) > 2:
            # print("here")

            for diff in nums_diff:
                conclusion.append(hash_map[diff])
        
            conclusion.sort()
            print("sorted: ", conclusion)
            
            for a in range(len(nums)):
                for b in range (a + 1, len(nums)):
                    if nums[a] + nums[b] == target:
                        return [a, b]
        else:
            print("here tis")
            if 'same' in hash_map:
                return [hash_map[nums[0]], hash_map['same']]
            else:
                return [0,1]
        
        # print("hash: ", hash_map)
        # print("conclusion: ", conclusion)


        