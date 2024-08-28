class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        ns=''
        sign = 1
        if s[0]=='-':
            sign = -1
            s = s[1:]
        
        ns = s[::-1]
        result =  int(ns)*sign

        if not(-2**31<=result<=2**31-1):
            return 0

        return result