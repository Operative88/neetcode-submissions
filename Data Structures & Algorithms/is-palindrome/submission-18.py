class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        
        
        t = [0] * 26

        r = s[::-1] 

        for a, b in zip(s, r):
            if a.isalnum():

                t[ord(a) - ord('a')] += 1
                t[ord(b) - ord('a')] -= 1


        return sum(t) == 0 
        



    