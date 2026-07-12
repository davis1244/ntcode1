from collections import Counter
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = [n for n in nums if n != val]
        nums[:] = new
        k = len(new)
        return k