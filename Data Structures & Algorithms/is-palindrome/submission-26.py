class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t = [0] * 500

        r = s[::-1] 

        

        for a in s:

            if a.isalnum():
            
                t[ord(a.lower()) - ord('a')] += 1
                t[r[ord(a.lower()) - ord('a')]] -= 1


        return sum(t) == 0 
        



    