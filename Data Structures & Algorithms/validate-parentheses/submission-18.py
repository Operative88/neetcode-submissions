class Solution:
    def isValid(self, s: str) -> bool:
        
        # "}}"
        pairs = {']': '[', '}': '{', ')': '('}
        seen = []
        
        for nawias in s:
            if nawias not in pairs:
                seen.append(nawias)
            
            elif not seen or seen.pop() != nawias:
                return False
        return True

