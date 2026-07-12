class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = max(nums, key=nums.count)
        return k




        