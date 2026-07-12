class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        seen = {}

        for i, j in enumerate(nums):
            difference = target - j
            if difference in seen:
                return [seen[difference], i]
            seen[j] = i





