class Solution:
    def isValid(self, s: str) -> bool:
        seen = [s[0]]
        open = {"[": 1, "{": 2, "(": 3}
        close = {"]": 1, "}": 2, ")": 3}
        for index in s[1:]:
            if index in open:
                seen.append(index)
            else:
                if close[index] != open[seen[-1]]:
                    return False
        return True


