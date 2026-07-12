class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash_table = defaultdict(list)

        for n in strs:
            sorted_s = tuple(sorted(n))
            hash_table[sorted_s].append(n)
            
        for v in hash_table.values():
            result.append(v)

        return result