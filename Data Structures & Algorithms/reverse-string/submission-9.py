class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # i = 0
        # j = len(s) - 1

        # while i < j:
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1

        # s.reverse()

        stack = []
        for c in s:
            stack.append(c)

        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
        return s
        
        
        
        
        

            
        