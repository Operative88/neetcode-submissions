class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        open = {"[": 1, "{": 2, "(": 3}
        close = {"]": 1, "}": 2, ")": 3}
        for index in s:
            if index in open:
                seen.add(index)
            else:
                if close[index] != open[seen[-1]]:
                    return False
        return True


