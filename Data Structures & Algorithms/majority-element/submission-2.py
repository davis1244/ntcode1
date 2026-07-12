class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # k = max(set(nums), key=nums.count)
        # return k

        nums.sort()
        return nums[len(nums) // 2]       
        