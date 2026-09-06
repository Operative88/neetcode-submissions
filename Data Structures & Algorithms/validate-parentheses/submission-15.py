class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {']': '[', '}': '{', ')': '('}
        seen = []
        
        for nawias in s:
            if nawias not in pairs:
                seen.add(nawias)
            
            elif seen.pop() != nawias:
                return False
        return True

