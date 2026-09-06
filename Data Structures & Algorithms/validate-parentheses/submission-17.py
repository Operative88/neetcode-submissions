class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {']': '[', '}': '{', ')': '('}
        seen = [1]
        
        for nawias in s:
            if nawias not in pairs:
                seen.append(nawias)
            
            elif seen.pop() != nawias:
                return False
        return True

