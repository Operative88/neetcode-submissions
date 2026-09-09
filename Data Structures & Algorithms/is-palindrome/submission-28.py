class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t = [0] * 26

        r = s[::-1] 

        #was it
        #was i c

        for a, b in zip(s, r):

            if a.isalnum(): #to jest źle - odwrócona lista nie zawsze ma spacje na tej samej pozycji, choc jest palindromem
            
                t[ord(a.lower()) - ord('a')] += 1
            if b.isalnum():    
                t[ord(b.lower()) - ord('a')] -= 1


        return sum(t) == 0 
        



    