from collections import Counter
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered_element = [n for n in nums if n != val]
        nums[:] = filtered_element
        k = len(nums)
        return k