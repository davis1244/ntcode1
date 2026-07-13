class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingKey = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closingKey:
                if stack and stack[-1] == closingKey[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False



            
            
            
        