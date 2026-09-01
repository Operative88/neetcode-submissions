class Solution:
    def isPalindrome(self, s: str) -> bool:

        czyste = [c.lower() for c in s if c.isalnum()]
        return czyste == czyste[::-1]
        