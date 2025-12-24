class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            a = x
            x = 0 
            while a > 0 : 
                x = x * 10 + a % 10 
                a //= 10
        else :
            a = -x
            x = 0
            while a > 0:
                x = x*10 + a%10
                a //= 10
            x = -x
        if x > 2**31 -1 :
            return 0
        if x <= -2**31 :
            return 0
        return x
            
            
