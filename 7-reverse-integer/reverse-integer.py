class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            n=str(x)
            n=n[1:]
            n=n[::-1]
            n="-"+n
            return int(n) if -2**31<=int(n)<=2**31-1 else 0
        else:
            n=str(x)
            n=n[::-1]
            k=int(n)
            return k if -2**31<=k<=2**31-1 else 0
        