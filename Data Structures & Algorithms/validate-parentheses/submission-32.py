class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {'}': '{', ')': '(', ']': '['}

        seen = []

        for nawias in s:
            if nawias not in pairs:
                seen.append(nawias)
            else:
                #if not seen or pairs[nawias] != seen.pop():
                #    return False 

                if not seen or pairs[nawias] != seen.pop():
                    return False

        #if len(seen) == len(s) or seen:
        #    return False
        #else:
        #    return True
        return not seen