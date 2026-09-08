class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [0] * 26

        for a, b in zip(s, t):
            if a.isalnum():
                t[ord(chr) - ord('a')] += 1
                t[ord(b) - ord('a')] -= 1


        return not t