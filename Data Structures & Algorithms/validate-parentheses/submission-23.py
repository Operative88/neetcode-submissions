class Solution:
    def isValid(self, s: str) -> bool:
        
        # "[(])"

        pairs = {']': '[', '}': '{', ')': '('}
        
        seen = []
        
        for nawias in s:
            if nawias not in pairs:
                seen.append(nawias)

            else:
                if pairs[nawias] != seen.pop():
                    return False
        return True
