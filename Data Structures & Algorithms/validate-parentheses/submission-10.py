class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {"]": "[", "}": "{", ")": "("}

        for ch in s:
            if ch not in pairs:
                seen.append(ch)
            elif not seen or seen.pop() != pairs[ch]:
                return False
        return not seen

