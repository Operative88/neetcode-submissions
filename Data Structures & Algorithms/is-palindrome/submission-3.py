class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [0] * 26

        for a, b in zip(s, t):
            if chr.isalnum():
                val[ord(chr) - ord('a')] += 1
                val[ord(b) - ord('a')] -= 1


        return not val