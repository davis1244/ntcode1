class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        hashtable = {}

        for i, k in enumerate(nums):
            diff = target - k
            if diff in hashtable:
                return [hashtable[diff], i]
            hashtable[k] = i

        
        

        
        






