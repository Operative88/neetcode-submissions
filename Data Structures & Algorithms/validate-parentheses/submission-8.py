class Solution:
    def isValid(self, s: str) -> bool:
        seen = [] # lista na nawias otwierający
        pairs = {"]": "[", "}": "{", ")": "("}

        for ch in s:
            if ch not in pairs: # czy jest nawiasem otwierającym?
                seen.append(ch) # dodaj go do listy

            elif not seen or seen.pop() != pairs[ch]: # dla nawiasu zamykającego sprawdź,
                                                     # czy lista jest pusta lub ostatni nawias 
                                                     # otwierający nie jest tego samego rodzaju
                return False
        return not seen

