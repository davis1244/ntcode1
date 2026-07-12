from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagrams[sorted_s].append(s)

        for v in anagrams.values():
            result.append(v)
        
        return result
        