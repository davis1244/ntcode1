class Solution:
    def isValid(self, s: str) -> bool:
        new = []
        closingKey = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in closingKey:
                if new and new[-1] == closingKey[c]:
                    new.pop()
                else:
                    return False
            else:
                new.append(c)
        return True if not new else False



            
            
            
        