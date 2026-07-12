class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)


        # if sorted_s == sorted_t:
        #     return True
        # return False
        
        if len(s) != len(t):
            return False

        counted_s, counted_t = {}, {}

        for i in range(len(s)):
            counted_s[s[i]] = 1 + counted_s.get(s[i], 0)
            counted_t[t[i]] = 1 + counted_t.get(t[i], 0)
        if counted_s == counted_t:
            return True
        return False