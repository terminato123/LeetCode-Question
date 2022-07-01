class Solution:
    def isUgly(self, n: int) -> bool:
        if not n:
            return False
        for k in [2,3,5]:
            while(n%k==0):
                n//=k
        return n==1
                
        