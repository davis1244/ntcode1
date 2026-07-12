class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        hash = set()

        for n in nums:
            if n in hash:
                return True
            hash.add(n)
        return False




