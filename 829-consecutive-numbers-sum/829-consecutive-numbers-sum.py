class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        c=0
        s=0
        for i in range(1,n+1):
            s+=i-1
            if s>=n:
                break
            if (n-s)%i==0:
                c+=1
        return c
                
        