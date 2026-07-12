class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # if sorted_s == sorted_t:
        #     return True
        # return False
        
        if len(s) != len(t):
            return False

        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        
        return hash_s == hash_t