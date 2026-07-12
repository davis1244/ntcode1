from collections import Counter
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = [n for n in nums if n != val]
        nums[:] = new
        k = len(new)
        return k

        k = 0 

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k