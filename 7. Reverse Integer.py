class Solution:
    def reverse(self, x: int) -> int:
        s=1
        if x<0:
            s=-1
            x=x*s
        x=str(x)
        t=x[::-1]
        x=int(t)
        
        if x<(-2)**31 or x>(2**31-1):
            return 0
        return x*s