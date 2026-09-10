class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = str(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]