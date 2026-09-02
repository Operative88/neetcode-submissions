class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' is s or '()' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
