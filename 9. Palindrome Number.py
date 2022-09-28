class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        t=str(x)
        t=t[::-1]
        
        
        if str(x)==t:
            return True
        else:
            return False